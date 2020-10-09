
#DYNAMIC PROGRAM
arr=list(map(int,input().split()))
n=len(arr)
s=int(input())
subset=[[False for i in range(n+1)]for j in range(s+1)]

count=[[0 for i in range(n+1)]for j in range(s+1)]

#if the set is empty
for i in range(n+1):
    subset[0][i]=True
    count[0][i]=0

for i in range(1,s+1):
    subset[i][0]=False
    count[i][0]=-1

for i in range(1,s+1):
    for j in range(1,n+1):
        subset[i][j]=subset[i][j-1]
        count[i][j]=count[i][j-1]
        if i>=arr[j-1]:
       
            subset[i][j]=(subset[i][j] or subset[i-arr[j-1]][j-1])

            if subset[i][j]:
                count[i][j]=max(count[i][j],count[i-arr[j-1]][j-1]+1)
#print(count[s][n])
for i in count:
    print(*i)

print()    
                
                
            
            
        
        