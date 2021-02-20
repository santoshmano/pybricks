#!/usr/bin/env python3
# Undirected Graph
#
class Graph:
    def __init__(self, n=0, edges=[]):
        self.adj = [[] for _ in range(n)]
        if edges:
            self.add_edges(edges)

    def add_edges(self, edges):
        for s, e in edges:
           self.adj[s].append(e)
           self.adj[e].append(s)

    def __str__(self):
        s = "\n"
        s += "Vertices: " + ''.join([str(i)+" " for i in range(len(self.adj))]) + "\n"
        for v in range(len(self.adj)):
            s += str(v) + ":" + str(self.adj[v]) + "\n"
        return s

def dfs(g):
    visited = set()
    for v in range(len(g.adj)):
        if v not in visited:
            _dfs(g, v, visited)
    return

def _dfs(g, v, visited):
    print(v)
    visited.add(v)
    for n in g.adj[v]:
        if n not in visited:
             _dfs(g, n, visited)

def dfs_iterative(g):
    visited = set()
    for v in range(len(g.adj)):
        if v not in visited:
            _dfs_iterative(g, v, visited)


def _dfs_iterative(g, v, visited):
    s = []  #simulating a stack using list

    s.append(v)
    visited.add(v)

    while s:
        v = s.pop()
        print(v)
        for n in reversed(g.adj[v]):
            if n not in visited:
                s.append(n)
                visited.add(n)
    return

def bfs(g):
    visited = set()
    for v in range(len(g.adj)):
        path=[]
        if v not in visited:
            _bfs(g, v, visited, path)
        print(path)

def _bfs(g, v, visited, path):
    q = []
    q.insert(0, v)
    visited.add(v)

    while q:
        v = q.pop()
        print(path)
        path.append(v)
        for n in g.adj[v]:
            if n not in visited:
                q.insert(0, n)
                visited.add(n)
    return


def test():
    g1 = Graph(3)
    g1.add_edges([(0,1),(2,1)])

    g2 = Graph(4, ((0,1), (0, 3), (2,1), (3, 2)))
    print("Graph g1:", g1)
    print("Graph g2:", g2)

    print("dfs of g1");
    dfs(g1)
    print("dfs iter of g1");
    dfs_iterative(g1)
    print("dfs of g2");

    dfs(g2)
    print("dfs iter of g2");
    dfs_iterative(g2)
    bfs(g2)

if __name__ == '__main__':
    test()