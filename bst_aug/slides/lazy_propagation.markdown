Lazy propagation
----------------

Let's consider another type of queries:

Given $k_1, k_2 \in K, v\in V$
associate all the keys $k: k_1 \leq k \leq k_2$
with value $v$

* * *

Lazy propagation
----------------

For array-based implementation
solution is to store in node ```cache```
along with value
and propagate it lazily
to childrens as you go down
