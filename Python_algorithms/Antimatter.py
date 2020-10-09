import sys

'''
def AM(a,m):
    if len(a)==1:
        return m
    m1=min(a)
    if m1<m:
        m=m1
    r=sorted(a)
    ret=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    
    return AM(ret,m)
a=[30,27,26,10,6]

print(AM(a,sys.maxsize))'''


def antimatter(a,n,s):
    if n==0:
        return s
#    return  min(antimatter(a,n-1,s), min(antimatter(a,n-1,abs(s-a[n-1])), min(antimatter(a,n-1,abs(s+a[n-1])),antimatter(a,n-1,a[n-1]))));       
    return  min(antimatter(a,n-1,s),antimatter(a,n-1,abs(s-a[n-1])),antimatter(a,n-1,abs(s+a[n-1])),antimatter(a,n-1,a[n-1]));       

a=[1,2,5,10,14]
print(antimatter(a,4,a[4]))

#a=[30,27,26,10,6]
#print(antimatter(a,4,a[4]))
