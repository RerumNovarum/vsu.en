RMQ (range minimum query)
---

Given array ```a[1..n]``` of $n$ objects of well-ordered set
for given $1 \leq l \leq r \leq n$ find the minimal element
in subarray ```a[l..r]```

. . .

A bit more complicated?

. . .

Actually much-much larger class of similar problems is solvable with generic approach! (stay tuned)

* * *

Simple solution is to remember
minimal values in whole array ```a[1..n]```,
subarray ```a[1..n/2], a[n/2+1..n]```, $\ldots$
(continuing splitting intervals, until $l=r$)

. . .

There are $n$ intervals of length 1,
floor($n/2$) intervals of length 2,
$\ldots$.

. . .

Total number of such segments is bounded by
$$\sum_k N/2^k = N \sum_k 2^{-k} = N \frac{1}{1-1/2} = 2N$$

Which means that we only need to use linear in $n$ space

. . .

Let ```cache(l, r)``` be precomputed
minimal value in subarray ```a[l..r]```
where $l$ and $r$ are powers of 2

. . .

Begining with $tl=1, tr=n$
we can solve task with simple recursive logic

* * *

```python
def rmq(l, r, tl, tr):
  if not intersects(l, r, tl, tr) or tl>tr: return INFINITY;
  if contains(l, r, tl, tr): return cache(l,r)
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
where firt node assigned to segment $1..n$,
it's children to segments $1..m$ and $m+1..n$ and so on.

* * *
