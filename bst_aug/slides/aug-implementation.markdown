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
Is based on local rotations,
so we can maintain auxiliary data
during them

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
        self.restore(h) # here we maintain aux
        h = self.balance(h) # and here too
        return h
```

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
