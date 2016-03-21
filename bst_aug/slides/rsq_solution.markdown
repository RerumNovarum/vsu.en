RSQ using array-based tree
---

Let's represent binary tree with array indices arithmetics:

* Each node is assigned a number $v$, which is index in array
* Root's index is $0$
* Left child of $v$ has index $2v+1$
* Right child of $v$ has index $2v+2$
* Parent of $v$ has index floor($(v-1)/2$)

* * *

RSQ using array-based tree (API)
---

```C++
template<typename T>
class RSQ {
  private:
    int n;
    int buffsize;
    T*  tree;
  public:
    RSQ(int n);
    ~RSQ();
    void put(int k, T v);
    T get(int k);
    T sum(int l, int r);
  private:
    // i
    put(int i, T v, int ti, int tl, int tr);
    T sum(int l, int r, int ti, int tl, int tr);
```

* * *

### Constructor ###

```C++
RSQ(int n) {
  this->n    = n;
  this->buffsize=4*n;
  this->tree = new T[this->buffsize];
  for (int i = this->buffsize - 1; i >= 0; --i) this->tree[i] = 0;
}
~RSQ() {
  delete[] this->tree;
}
```
* * *

### Retrieving ###

```C++
T get(int l, int r, int ti, int tl, int tr) {
  if (ti >= this->buffsize) return 0;
  if (tl > tr) return 0;
  if (l <= tl && tr <= r) return this->tree[ti];
  int m = (tl+tr)/2;
  T s = 0;
  if (intersects(l, r, tl, m))   s += get(l, r, left(ti),  tl,  m);
  if (intersects(l, r, m+1, tr)) s += get(l, r, right(ti), m+1, tr);
  return s;
}
```

* * *

### Updating ###
```C++
void set(int i, T v, int ti, int l, int r) {
  if (ti >= this->buffsize) return;
  if (l>r)  return;
  if (l==r) {
    this->tree[ti] = v;
  }
  else {
    int m = (l+r)/2;
    if (i <= m) set(i, v, left(ti),  l,   m);
    else        set(i, v, right(ti), m+1, r);
    this->tree[ti] = this->tree[left(ti)] + this->tree[right(ti)];
  }
}
```

* * *
