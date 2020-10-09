import time
from itertools import combinations_with_replacement as c
from functools import lru_cache
from collections import defaultdict as dd

cache1={}
def soe(n):
    if n in cache1:
        return cache1[n]
    v=[1 for i in range(n+2)]
    v[1],v[0]=0,0
    for i in range(2,int(n**0.5)+1):
        j=2
        if v[i]==1:
            while j*i<=n:
                
                v[j*i]=0
                j+=1
                
                
    f=bool(v[n]==1)
    
    cache1[n]=f
    return f
        


def sum_digit(n):
    r=0
    while n//10!=0:
        r=r+n%10
        n=n//10
    return r
@lru_cache(1000)
def final(n):
    a=[i for i in range(0,n+1)]
    c1=0
    for i in c(a,2):
        if soe(sum(i)):
            
            c1+=1
    return c1
s=time.time()
print(final(int(10000)))
e=time.time()
print("time:",e-s)



