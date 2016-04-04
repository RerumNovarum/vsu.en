BLACK, RED = False, True
def is_red(h):
    return h.c if h else BLACK
class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.c         = RED
        self.l, self.r = None, None
    def __str__(self):
        return '(%s, %s, %s)'%(k, v, 'RED' if self.c else 'BLACK')
    def __repr__(self): return self.__str__()
class RBBST:
    def __init__(self):
        self.root = None
        self.Node = Node
    def restore(self, h):
        """restore(h)
h:  root of subtree
used in derived datastructures to update cumulative values"""
        return h
    def rotation_fix(self, x, h): 
        """rotation_fix(x, h)
x:  new (post-rotation) root of subtree
h:  old root
just fixed colors"""
        x.c = h.c
        h.c = RED
    def balance(self, h):
        """balance(h)
h:  root of subtree
return value:   new root of balanced subtree
used to locally balance subtree (simulating 2-3-tree)"""
        assert not h is None
        if is_red(h.r) and not is_red(h.l):
            h = self.rotate_left(h)
        if is_red(h.l) and is_red(h.l.l):
            h = self.rotate_right(h)
        if is_red(h.l) and is_red(h.r):
            self.flip_colors(h)
        return h
    def put(self, k, v):
        """put(k, v)
$k \\in K$ where $K$ is totally ordered set of keys
$v \\in M$ where $M$ is set of values
associates value $v$ with key $k$"""
        self.root   = self.subtree_put(self.root, k, v)
        self.root.c = BLACK
    def subtree_put(self, h, k, v):
        """subtree_put(h, k, v)
h:  root of subtree
k:  key
v:  value
recursive method to insert new kv-pair into tree
and maintain balance"""
        if h is None: return self.Node(k, v)
        if k < h.k:     h.l = self.subtree_put(h.l, k, v)
        elif h.k < k:   h.r = self.subtree_put(h.r, k, v)
        else:           h.v = v
        self.restore(h)
        h = self.balance(h)
        return h
    def __get__(self, h, k):
        """__get__(h, k)
h:  root of subtree
k:  queried key
TODO: should be rewritten as iterative"""
        if h is None:   return
        if k < h.k:     return self.__get__(h.l, k)
        elif h.k < k:   return self.__get__(h.r, k)
        else:           return h.v
    def get(self, k):
        """get(k)
$k\\in K$ where K is totally ordered set of keys
returns value $v\\in M$ associated with key $k$ if any"""
        return self.__get__(self.root, k)
    def rotate_left(self, h):
        """rotate_left(h)
rotates left the edge (h, h.r) and returns new root"""
        assert not h is None and is_red(h.r)
        x       = h.r
        h.r     = x.l
        x.l= h
        self.rotation_fix(x, h)
        return x
    def rotate_right(self, h):
        """rotate_right(h)
rotates right the edge (h, h.l) and returns new root"""
        assert not h is None and is_red(h.l)
        x       = h.l
        h.l     = x.r
        x.r     = h
        self.rotation_fix(x, h)
        return x
    def flip_colors(self, h):
        h.l.c = h.r.c = h.c
        h.c = not h.c
