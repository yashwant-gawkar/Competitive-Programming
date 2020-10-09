def permutation(s,left,right):
    if left==right:
        print(s)
        return
    else:
        for i in range(left,right):
            s[left],s[i]=s[i],s[left]
            
            permutation(s,left+1,right)
            
            s[left],s[i]=s[i],s[left]
            

        
        
a=[1,2,3]
permutation(a,0,3)