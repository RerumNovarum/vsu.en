Arbitrary keys
--------------

Now let's make our task a bit trickier
and say, that we want, for example,
say that keys are points in time or whatever
with total order defined on it,
instead of indices of array

And like before we want
to perform

* ```put(k, v)```
* ```get(l, r)```

reasonably fast

* * *

Arbitrary keys
--------------

Since key's aren't integers bounded by some small constant,
we can't use key as index in array

What to do?

. . .

We need some ordered Symbol Table

. . .

Binary Search Tree!

. . .

Can we handle range queries anyhow but bruteforcing?

. . .

YES!

* * *
