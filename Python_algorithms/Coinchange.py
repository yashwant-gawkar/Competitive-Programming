memo={}

def change(n,c):
    if n==0:
        return 1
    if n<0:
        return 0
    if (n,len(c)) in memo:
        return memo[(n,len(c))]
    c_sum=0
    for i in range(len(c)):
        c_item=c[i]
        
        c_sum+=change(n-c_item,c[i:])
        
    memo[(n,len(c))]=c_sum
    
    return c_sum

print(change(4,[1,2]))
    