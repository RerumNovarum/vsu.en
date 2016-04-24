Array-based segments tree
-------------------------

Simple solution is to remember each value `v[i]`,
then minimal value `m(2*k, 2*k+1)` in each pair `(v[2*k], v[2*k+1])`,
then minimal value `m(4*k, 4*k+3)` and so on

Then answer can be found in logarithmic time

```
+------------------------------------------+
|                m(0,n-1)                  |
+------------------------------------------+
|                   ...                    |
+--------------------+---------------------+
|       m(0,3)       |         ...         |
+----------+---------+---------------------+
| m(0,1)   | m(2,3)  |         ...         |
+------+---+--+------+------+-----+--------+
| v[0] | v[1] | v[2] | v[3] | ... | v[n-1] |
+------+------+------+------+-----+--------+
```

* * *

There are $n$ intervals of length 1,
floor($n/2$) intervals of length 2,
$\ldots$.

. . .

Total number of such segments is bounded by
$$\sum_k N/2^k = N \sum_k 2^{-k} = N \frac{1}{1-1/2} = 2N$$

Which means that we only need to use space linear in $n$

. . .

Let ```s(l, r)``` be precomputed
minimal value in subarray ```a[l..r]```
where $l$ and $r$ are powers of 2

. . .

Begining with $tl=0, tr=n-1$
we can solve task with simple recursive logic

* * *

```python
def rmq(l, r, tl, tr):
  if not intersects(l, r, tl, tr) or tl>tr: return INFINITY;
  if contains(l, r, tl, tr): return s(l,r)
  m = (tl+tr)//2
  infimum = INFINITY
  if intersects(l, r, tl, m):
    infimum = min(infimum, rmq(l, r, tl, m))
  if intersects(l, r, m+1, tr):
     infimum = min(infimum, rmq(l, r, m+1, tr))
  return infimum
```

* * *

RMQ
---

Such cache can be easily represented with binary tree,
where first node is assigned to segment $[0,n-1]$,
it's children to segments $[0,m-1]$ and $[m,n-1]$ and so on.

* * *
