#!/usr/bin/env python3

class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class DiGraph:
    def __init__(self, n, edges):
        self.vertices = [Vertex(i) for i in range(n)]
        self.add_edges(edges)

    def add_edges(self, edges):
        for s, e in edges:
            self.vertices[s].neighbors.append(self.vertices[e])

    def __str__(self):
        s = "Vertices - " + ''.join([" "+str(v.val) for v in self.vertices])
        for v in self.vertices:
            s += "\n" + str(v.val) + ":" + "".join([str(n.val)+"," for n in v.neighbors])
        return s


def clone_graph(graph):
    clone_graph = DiGraph(0, [])

    for v in graph.vertices:
        clone_map = {}
        if v not in clone_map:
            clone_vertex(graph, v, clone_map)
        clone_graph.vertices.append(clone_map[v])

    return clone_graph

def clone_vertex(g, v, clone_map):
    clone_v = Vertex(v.val)
    clone_map[v] = clone_v

    for n in v.neighbors:
        if n not in clone_map:
            clone_v.neighbors.append(clone_vertex(g, n, clone_map))
        else:
            clone_v.neighbors.append(clone_map[n])

    return clone_v


def test():
    g = DiGraph(3, [(0,2),(1,2),(2,0),(2,1),(1,0)])
    print(g)
    c = clone_graph(g)
    print(c)


if __name__ == "__main__":
    test()

