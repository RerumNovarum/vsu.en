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
