from collections import defaultdict as dd

class Graph:
    def __init__(self):
        self.graph=dd(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
     
    def bfs(self,s,d,c):
        v=[]
        if d in self.graph[s]:
            
            return c
        for i in self.graph[s]:
            v=self.bfs(i,d,c+1)
        return v
        
                 
            
            
        
                

for _ in range(int(input())):
    n,e=map(int,input().split())
    g=Graph()
    large=[]
    for i in range(e):
        large.append(list(map(int,input().split())))

    source=int(input())
    s_set=set(i[1] for i in large if i[0]==source)
    n_l=[[i[1],i[0]] for i in large if i[1] in s_set and i[0]!=source] 
    nn_l=[[i[0],i[1]] for i in large if i[1] not in s_set or i[0]==source]
    n_l.extend(nn_l)
    

    

  
    for i in n_l:

        g.addEdge(i[0],i[1])
        

    r=[]
    for i in range(1,n+1):
        c=0
        if i==source:
            continue

        
        c+=1
        
        r.append(g.bfs(source,i,c))
    for i in range(len(r)):
        if r[i]==[]:
            r[i]=-1
        else:
            r[i]*=6
    print(*r)

    

    
                

