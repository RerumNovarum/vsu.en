Augmenting search trees
-----------------------

Let's say we implemented
red-black BST with following API:

```python
class Node:
    def __init__(self, k, v): pass
class RBBST:
    def __init__(self):
      self.Node = Node # to be overriden
      pass
    def restore(self, h): pass # to be overriden
    def balance(self, h): pass
    def put(self, k, v):  pass
    def get(self, k):     pass
    def rotate_left(self, h): pass
    def flip_colors(self, h): pass
    def rotation_fix(self, x, h):  pass
```

* * *

Augmenting search trees
-----------------------

Here ```balance``` performs required rotations
calls ```restore``` if necessary
and returns new root of subtree
It is called during insertion in following manner:

* * *

Augmenting search trees
-----------------------

```python
    def __put__(self, h, k, v):
        """__put__(h, k, v)
h:  root of subtree
k:  key
v:  value
recursive method to insert new kv-pair into tree
and maintain balance"""
        if h is None: return self.Node(k, v)
        if k < h.k:     h.l = self.__put__(h.l, k, v)
        elif h.k < k:   h.r = self.__put__(h.r, k, v)
        else:           h.v = v
        self.restore(h)
        h = self.balance(h)
        return h
```

We will augment tree by overriding ```Node``` class
and ```restore``` method

* * *

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

SegmentTree (API)
-----------------

```python
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
def add(x, y): return x+y
t = SegmentTree(add, '')
t.put(1, 'some ')
t.put(10**32, 'strings') # we can use some large 'indices'* * *
t.put(-10**9, 'concat ')
t.mul(-10**64, 10**64)   # yields 'concat some strings'
```

* * *

SegmentTree Node
----------------

```python
class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v # key, value
        self.c         = RED  # color
        self.l, self.r = None, None # segment [l,r] represented by Node
    def __str__(self):
        return '(%s, %s, %s)'%(k, v, 'RED' if self.c else 'BLACK')
    def __repr__(self): return self.__str__()
```

* * *

SegmentTree maintaining aux data
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
    def __mul__(self, h, l, r):
        """__mul__(h, l, r)
calculates cumulative in intersection of (h.lk, h.rk) and (l, r)"""
        s = self.id
        if l <= h.lk <= h.rk <= r: return h.mul
        if h.l and intersects(h.l.lk, h.l.rk, l, r):
            s = self.mulbin(self.__mul__(h.l, l, r), s)
        if l <= h.k <= r:
            s = self.mulbin(s, h.v)
        if h.r and intersects(h.r.lk, h.r.rk, l, r):
            s = self.mulbin(s, self.__mul__(h.r, l, r))
        return s
```
