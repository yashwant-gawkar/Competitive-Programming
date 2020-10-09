from collections import defaultdict as dd
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 01:54:21 2020

@author: User
"""

class Graph:
    def __init__(self):
        self.graph=dd(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfsUtil(self,v,visited):
        visited[v]=True
        
        print(v)
    
            
        
        for i in self.graph[v]:
            if visited==False:
                self.dfsUtil(i,visited)  
                
    def dfs(self):
        V=len(self.graph)
        visited=[False for i in range(V+1)]
        for i in range(V):
            if visited[i]==False:
                self.dfsUtil(i,visited)
                
g=Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  

g.dfs() 
            