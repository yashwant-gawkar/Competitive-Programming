def coin_max(a,l,r):
    if l+1==r:
        return max(a[l],a[r])
    return max(a[l]+min(coin_max(a,l+2,r),coin_max(a,l+1,r-1)),a[r]+min(coin_max(a,l+1,r-1),coin_max(a,l,r-2)))

a=[1,2,200,1000 ]

print(coin_max(a,0,3))