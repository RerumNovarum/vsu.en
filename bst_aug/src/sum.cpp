#include <iostream>
#include <fstream>

template<typename T>
T min(T a, T b) {
  return a <= b ? a : b;
}
template<typename T>
T max(T a, T b) {
  return a >= b ? a : b;
}
template<typename T>
bool intersects(T a1, T a2, T b1, T b2) {
  return (a1 <= b1 && b1 <= a2) || (b1 <= a1 && a1 <= b2);
}

template<typename T>
class RSQ {
  private:
    int n;
    int buffsize;
    T*  tree;
  public:
    RSQ(int n) {
      this->n    = n;
      this->buffsize=4*n;
      this->tree = new T[this->buffsize];
      for (int i = this->buffsize - 1; i >= 0; --i) this->tree[i] = 0;
    }
    ~RSQ() {
      delete[] this->tree;
    }
    void set(int i, T v) {
      this->set(i, v, 0, 0, this->n-1);
    }
    T get(int l, int r) {
      return this->get(l, r, 0, 0, this->n-1);
    }
    T sum(int i, int j) {}
  private:
    static inline int left(int i) {
      return 2*i + 1;
    }
    static inline int right(int i) {
      return 2*i + 2;
    }
    static inline int parent(int i) {
      return (i-1)/2;
    }
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
    T get(int l, int r, int ti, int tl, int tr) {
//      std::cout << "l=" << l << ", r=" << r << ", ti=" << ti << ", tl=" << tl << ", tr=" << tr << std::endl;
      if (ti >= this->buffsize) return 0;
      if (tl > tr) return 0;
      if (l <= tl && tr <= r) return this->tree[ti];
      int m = (tl+tr)/2;
      T s = 0;
      if (intersects(l, r, tl, m))   s += get(l, r, left(ti),  tl,  m);
      if (intersects(l, r, m+1, tr)) s += get(l, r, right(ti), m+1, tr);
      return s;
    }
};

int main() {
  int n, q;
  std::ifstream in;
  std::ofstream out;
  in.open("sum.in");
  out.open("sum.out");
  in >> n >> q;
  RSQ<long long> rsq(n);
  std::string Q_GET="Q", Q_SET="A";
  for (int i = 0; i < q; ++i) {
    std::string cmd;
    in >> cmd;
    if (cmd == Q_GET) {
      int l, r;
      in  >> l >> r;
      out << rsq.get(l-1, r-1) << std::endl;
    } else if (cmd == Q_SET) {
      int i;
      long long v;
      in  >> i >> v;
      rsq.set(i-1, v);
    }
  }
  in.close();
  out.close();
  return 0;
}
