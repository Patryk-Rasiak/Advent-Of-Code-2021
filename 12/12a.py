from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0

    def addEdge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def countAllPathsRec(self, u, d, visited, path):

        # Mark the current vertex as visited and store in path
        if u.islower():
            visited[u] = True

        path.append(u)

        # If current vertex is same as destination, then increment number of paths
        if u == d:
            self.count += 1
        else:
            # Recur for all the vertices adjacent to this vertex
            for v in self.graph[u]:
                if visited[v] == False:
                    self.countAllPathsRec(v, d, visited, path)

        # Remove current vertex from the path and mark it as unvisited
        path.pop()
        visited[u] = False

    def countAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = {key: False for key in self.graph.keys()}

        path = []

        self.countAllPathsRec(s, d, visited, path)


# Graph with every cave as the vertex
g = Graph()

with open("advent/12/12a.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]


for line in data:
    a, b = line.split("-")
    g.addEdge(a, b)
    g.addEdge(b, a)


g.countAllPaths("start", "end")
print(g.count)
