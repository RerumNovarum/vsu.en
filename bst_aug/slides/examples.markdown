Examples
========

Range-query
-----------

> Range-minimum, range-maximum, range-sum and range-whatever queries

Solution:
Store ``multiple'' in node

Order statistics
----------------

1. > For given key `k` find it's position
   > in ordered sequence of all the keys in the tree
2. > For given position `j`
   > find key `k_j` at this position
   > in ordered sequence of all the keys in the tree

Solution:
Store size of subtree in each node

* * *
