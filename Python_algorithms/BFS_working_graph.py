import sys
class Vertex:
    def __init__(self,n):
        self.distance=sys.maxsize
        self.colour="black"
        self.name=n
        self.neighbours=[]
    def add_neighbour(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
    
class Graph:
    def __init__(self):
        self.vertices={}
    def add_vertex(self,v):
        if isinstance(v,Vertex) and v not in self.vertices:
            self.vertices[v.name]=v
    def add_edge(self,u,v):
        self.vertices[u].add_neighbour(v)
        self.vertices[v].add_neighbour(u)
    def print_graph(self):
        for i in self.vertices:
            v=self.vertices[i]
            print(str(i)+str(v.neighbours)+""+str(v.distance))
    def BFS(self,v):
        queue=[]
        vert=self.vertices[v]
        vert.distance=0
        for i in vert.neighbours:
            self.vertices[i].distance=vert.distance+1
            queue.append(i)
        while queue:
            u=queue.pop()
            vert_u=self.vertices[u]
            vert_u.colour="white"
                
            for i in vert_u.neighbours:
                vert_v=self.vertices[i] 
                if vert_v.colour=="black":
                    queue.append(i)
                    if vert_v.distance>vert_u.distance+1:
                        vert_v.distance=vert_u.distance+1
g=Graph()
v=Vertex(1)
for i in range(1,5):
    g.add_vertex(Vertex(i))
e=[[1,2],[1,3],[3,4]]
for i in e:
    g.add_edge(i[0],i[1])
g.BFS(3)
g.print_graph()

                        
