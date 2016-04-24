Augmenting search trees
-----------------------

To insert into BST:

* Choose subtree to go
* Call 'insert' for it recursively
* Update aux data based on children's aux

* * *

Augmenting search trees
-----------------------

Balancing?
Is based on rotations, these are local operations,
so we can maintain auxiliary data
during them

* * *

Augmenting search trees
-----------------------

Say red-black tree is implemented in recursive manner,
with e.g. insertion looking like this:
```python
    def subtree_put(self, h, k, v):
        """subtree_put(h, k, v)
h:  root of subtree
k:  key
v:  value"""
        if h is None: return self.Node(k, v)
        if k < h.k:     h.l = self.subtree_put(h.l, k, v)
        elif h.k < k:   h.r = self.subtree_put(h.r, k, v)
        else:           h.v = v
        self.restore(h)
        h = self.balance(h)
        return h
```

* * *

We can upgrade it to serve for range-queries
by augmenting `Node` and overriding `restore()`

SegmentTree (API)
-----------

```python
class SegmentTree(rbbst.RBBST):
    """SegmentTree(mul, id)
mul:    multiplication operation (callable, binary)
id:     identity element
*   put(k, v) where $k\\in K, v\\in M$
        associates key 'k' with value 'v'
*   get(k)  where $k\\in K$
        retrieve value associated with key 'k' if any
*   mul(l, r) where $l,r\\in K$ and $l\\leq r$"""
```

* * *

SegmentTree (Sample client)
-----------------

```python
# SegmentTree for Monoid of numbers
# with regular addition operation
# and 0 as identity element
def add(x, y): return x+y
t = SegmentTree(add, 0) 
t.put('a', 1) # associate value 1 with key 'a'
t.put('b', 3)
t.put('c', 22)
t.mul('a', 'c') # -> 26
t.mul('a', 'a') # -> 1
```

* * *

SegmentTree (API)
-----------------

```python
# SegmentTree for Monoid of strings
# with associative operation of concatenation
# and empty string as identity element
def add(x, y): return x+y
t = SegmentTree(add, '')
t.put(1, 'some ')
t.put(10**32, 'strings') # we can use some large 'indices'
t.put(-10**9, 'concat ')
t.mul(-10**64, 10**64)   # yields 'concat some strings'
```

* * *

SegmentTree (Augmentation)
--------------------------

We'll augment each node `h`
to store multiple 'h.mul'
of elements in range from 'h.lk' through 'h.rk'

```python
class Node(rbbst.Node):
    def __init__(self, k, v):
        super(Node, self).__init__(k, v)
        # we insert every new `Node` as a leaf
        # so it represents segment [k,k]
        self.lk  = self.rk = k
        # and multiple in this segment is simply `v`
        self.mul = v
```


* * *

SegmentTree (Maintaining aux data)
--------------------------------

```python
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
```

* * *

SegmentTree query
-----------------

```python
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
```
