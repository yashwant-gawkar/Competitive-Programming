import time
from functools import lru_cache
@lru_cache(maxsize=1000)
def fib(n):
   
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
    
start=time.time()
for i in range(1,10000):
    print(i,fib(i))
end=time.time()
print("time:",end-start)