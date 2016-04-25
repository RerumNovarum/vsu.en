Augmentation
------------

The idea is following:

If you're considering node $n$,
which represents range ```[n.lk, n.rk]```,
and you know the multiple ```n.l.mul```
of values with keys in range ```n.l.lk, n.l.rk```
and multiple of ```n.r.mul```
of values with keys in range ```n.r.lk, n.r.lk```,
then simply ```n.mul = n.l.mul * n.v * n.r.mul```

* * *

Augmentation
------------

More generally,
if range $l..r$ is requested,
and we're in node $n$,
then we either

* return $0$ if $[n.lk, n.rk]\cap [l,r] = \emptyset$
* return ```n.mul``` if  $[n.lk, n.rk] \subset [l,r]$
* recursively go into childrens and combine answers and value in current node

* * *

Augmentation theorem
--------------------

Let $K$ be totally-ordered set
and $(M, \circ, 1)$ be monoid
and let $T\subset M$ note values in tree.

Then following operations can be performed
in time logarithmic in input size
just by storing additional data in the nodes of tree
and maintaining this data during rotations:

* ```put(k, v)```
    Associate key $k$ with value $v$
* ```mul(l, r)```
    Calculate $v_{k_1}\circ v_{k_2} \circ \cdots \circ v_{k_m}$,
    where $v_{k_j}\in M\cap T$ and

     $l, r, k_j\in K$ and $l\leq k_j \leq r$ and $k_i\leq k_j$ for all $i\leq j=\overline{1,m}$

* * *

Go deeper
---------

We're not actually restricted
to use values set' monoid structure.

* Let $(K, \odot, I)$ be monoid too

* Their cartesian product $K\times M$
  with product $\otimes=(\odot,\circ)$
  and identity $J=(I, 1)$
  is a monoid as well

* We can maintain $\odot$-multiple of keys in range
  in the same manner as multiple of values
  or, equivalently, $\otimes$-multiple of key-value pairs


* * *

Actually, later we'll mainly ignore this formalisation
and will say, that we just maintain some Node invariants

* * *
