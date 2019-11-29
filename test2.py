from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def find_shortest_path(self,start, end, path):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


n=int(input())
y=[]
path=[]
for _ in range(n):
    y.append(int(input()))
g=Graph(n)
t=int(input())
for _ in range(t):
    a,b=list(map(int,input().split()))
    g.addEdge(a,b)
s=int(input())
d=int(input())
j=g.find_shortest_path(s,d,path)
print(*j)
