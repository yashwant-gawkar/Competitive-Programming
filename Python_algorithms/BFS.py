from collections import defaultdict as dd

class Graph:
    def __init__(self):
        self.graph=dd(list)
    def addEdge(self,u,v):   #*********IMPORTANT************
        self.graph[u].append(v)  #mistake
    
    def BFS(self,s,d):
        if s==d:                  #MAIN FUNCTION OF BFS
            return True
        
        queue=[]
        queue.append(s)
        visited=[False for i in range(len(self.graph)+10)]
        
        visited[s]=True    #forgot
        while(queue):
            s=queue.pop(0)
            
            for i in self.graph[s]:
                if i==d:
                    return True
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        return False



def isSafe(mat,i,j):
    if i>=0 and i<=len(mat) and j>=0 and j<=len(mat):
        return True
    return False

def pathFinder(mat):         #Steps:create graph->create k(matrix element counter)->
                             #find s,d->BFS 
    
    g=Graph()
    k=1
    N=len(mat)
    s,d=None,None
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0:
                if isSafe(mat,i,j+1):
                    g.addEdge(k,k+1)     #call addEdge dont do manually
                if isSafe(mat,i,j-1):
                    g.addEdge(k,k-1)
                if isSafe(mat,i+1,j):
                    g.addEdge(k,k+N)
                if isSafe(mat,i-1,j):
                    g.addEdge(k,k-N)
            if mat[i][j]==1:
                s=k             #s,d are in k value not in matrix value
            if mat[i][j]==2:
                d=k
            k+=1
    return g.BFS(s,d)





n=int(input("matrix size:"))
a=[]
for i in range(n):
    a.append(list(map(int,list(input()))))
print(pathFinder(a))
    
                    
                    


                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
             