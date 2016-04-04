import rbbst

def intersects(x1, x2, y1, y2):
    return x1 <= y1 <= x2 or y1 <= x1 <= y2
class Node(rbbst.Node):
    def __init__(self, k, v):
        super(Node, self).__init__(k, v)
        self.lk  = self.rk = k  # initially cumulative represents segment (k,k)
        self.mul = v            # and this cumulative is simply self.v
    def __str__(self):
        return '(k=%s v=%s clr=%s from %s to %s)'%\
                tuple(repr(x) for x in\
                (self.k, self.v, 'RED' if self.c else 'BLACK', self.lk, self.rk))
class SegmentTree(rbbst.RBBST):
    """SegmentTree(mul, id)
mul:    multiplication operation (callable, binary)
id:     identity element
Constructs dynamic Segment Tree based on red-black bst.
Acts just like dictionary (map)
but also supports specific range operations in logarithmic time.
Specifically:
Let (M, mul, id) be monoid
    (i.e. mul is associative binary operation on M
     and id be identity element regarding this operation)
    and K be totally-ordered set.
Then this datastructure can accomplish following tasks in O(log N):
*   put(k, v) where $k\\in K, v\\in M$
        associates key 'k' with value 'v'
*   get(k)  where $k\\in K$
        retrieve value associated with key 'k' if any
*   mul(l, r) where $l,r\\in K$ and $l\\leq r$
        calculates $v_1*v_2*\\ldots*v_n$
        where $x*y$ is shortcut for $mul(x,y)$
              (note, parentheses don't matter, since mul is associative)
              and $v_1, \ldots, v_n \\in M$ are all values
              with keys in range (l, r) inclusive
              ordered by their keys

* * *

Example:
    ```
    def add(x, y): return x+y
    t = SegmentTree(add, 0)
    t.put('a', 1) # associate value 1 with key 'a'
    t.put('b', 3)
    t.put('c', 22)
    t.mul('a', 'c') # -> 26
    t.mul('a', 'a') # -> 1
    ```

    ```
    def add(x, y): return x+y
    t = SegmentTree(add, '')
    t.put(1, 'some ')
    t.put(10**32, 'strings') # we can use some large 'indices'
    t.put(-10**9, 'concat ')
    t.mul(-10**64, 10**64)   # yields 'concat some strings'
    ```

"""
    def __init__(self, mul, id):
        """SegmentTree(mul, id)
id:     identity element
mul:    multiplication operation (callable, binary)"""
        super(SegmentTree, self).__init__()
        self.id, self.mulbin = id, mul
        self.Node = Node
    def restore(self, h):
        """restore(h)
overrided `restore` will update cumulative
after insertions and balancing"""
        assert not h is None
        h.lk, h.rk = h.k, h.k
        m = h.v
        if h.l:
            m = self.mulbin(h.l.mul, m)
            h.lk = h.l.lk
        if h.r:
            m = self.mulbin(m, h.r.mul)
            h.rk = h.r.rk
        h.mul = m
    def rotation_fix(self, x, h):
        """rotation_fix(x, h)
gonna maintain cumulative during rotations"""
        super(SegmentTree, self).rotation_fix(x, h)
        self.restore(h)
        self.restore(x)
    def mul(self, l, r):
        """mul(l, r)
$l \\leq r \\in K$ where $K$ is totally ordered set of keys
returns multiple of all values $v\\in M$
with keys in range (l, r) inclusive,
where (M, mul) is monoid"""
        return self.subtree_mul(self.root, l, r) if self.root else self.id
    def subtree_mul(self, h, l, r):
        """subtree_mul(h, l, r)
calculates cumulative in intersection of (h.lk, h.rk) and (l, r)"""
        s = self.id
        if h is None: return s
        if l <= h.lk <= h.rk <= r: return h.mul
        if h.l and intersects(h.l.lk, h.l.rk, l, r):
            s = self.mulbin(self.subtree_mul(h.l, l, r), s)
        if l <= h.k <= r:
            s = self.mulbin(s, h.v)
        if h.r and intersects(h.r.lk, h.r.rk, l, r):
            s = self.mulbin(s, self.subtree_mul(h.r, l, r))
        return s
