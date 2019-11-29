from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V= vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def find_path(self, start, end, path):
		path = path + [start]
		if start == end:
			return path
		if start not in self.graph:
			return None
		for node in self.graph[start]:
			if node not in path:
				newpath = self.find_path(node, end, path)
				if newpath: return newpath
		return None


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
j=g.find_path(s,d,path)
if j==None:
	print("0")
else:
	print("1")


# 4
# 2
# 5
# 7
# 9
# 4
# 2 9
# 7 2
# 7 9
# 9 5
# 7
# 5
