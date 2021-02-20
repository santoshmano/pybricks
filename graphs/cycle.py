#!/usr/bin/env python3
class DiGraph:
    def __init__(self, n, edges):
        self.adj = [[] for _ in range(n)]
        self.add_edges(edges)

    def add_edges(self, edges):
        for s, e in edges:
            self.adj[s].append(e)

    def __str__(self):
        s = "\n"
        s += "Vertices: " + ''.join([str(i)+" " for i in range(len(self.adj))]) + "\n"
        for v in range(len(self.adj)):
            s += str(v) + ":" + str(self.adj[v]) + "\n"
        return s

def has_cycle(g):
    visited = set()
    for v in range(len(g.adj)):
        if v not in visited:
            if _has_cycle(g, v, visited, []):
                return True
    return False

def _has_cycle(g, v, visited, path):
    if v in path:
        return True

    if v in visited:
        return False

    path.append(v)
    visited.add(v)

    # process its neighbors
    for n in g.adj[v]:
        if _has_cycle(g, n, visited, path):
            return True

    path.pop()
    return False

# print all the cycles in the graph
def all_cycles(g):
    return

def test():
    g1 = DiGraph(5, [(0,1),(1,2),(2,3),(3,4),(4,0)])
    g2 = DiGraph(5, [(0,1),(1,2),(2,3),(3,4)])
    g3 = DiGraph(5, [(0,1),(1,2),(2,3),(3,4),(4,3)])

    for g in g1, g2, g3:
        if has_cycle(g):
            print("The below graph has a cycle - ", g)

if __name__ == "__main__":
    test()
