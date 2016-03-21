import sys
import random

n = int(sys.argv[1])
k = n+n*(n+1)//2 # 10**5 # 
print('%d %d'%(n, k))
for i in range(n):
    print ('A %d %d'%(i+1, random.randint(10**8,10**9)))
    k -= 1
for i in range(n):
    for j in range(i, n):
        print('Q %d %d'%(i+1, j+1))
        k -= 1
        if k <= 1: break
    if k <= 1: break
print('Q 1 %d'%n)
