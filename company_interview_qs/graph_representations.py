
# Adjacency list
#


class Graph_1:
    def __init__(self):
        self.vertices = []
        self.edges = []

# hashmap of vertex -> neigbors
Graph_2 = {}

class Graph:
    def __init__(self):
        self.vertices = []

class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


def dfs(graph):
    visited = set()
    for v in graph.vertices:
        if v not in visited:
            _dfs(v, visited)

def _dfs(v, visited):
    # process v and add to visited set
    print(v.val)
    visited.add(v)

    # traverse its neighbors
    for n in v.neighbors:
        if n not in visited:
            _dfs(n, visited)

#
# Adjacency matrix
