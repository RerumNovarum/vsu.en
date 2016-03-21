RSQ (range sum query)
---

Given array ```a[1..n]``` of $n$ numbers
for given $1 \leq l \leq r \leq n$
calculate the sum of all numbers
in subarray ```a[l..r]```

. . .

In offline-variation
simple preprocessing (calculating cumulative partial sums)
in $O(n)$ time
allows to answer any such query in $O(1)$ time

. . .

```python
def rsq(l, r):
  return cumsum[r] - (cumsum[l-1] if l != 0 else 0)
```
