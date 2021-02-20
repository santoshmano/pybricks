class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class DiGraph:
    def __init__(self, n, edges):
        self.vertices = [Vertex(i) for i in range(n)]
        self.add_edges(edges)

    def add_edges(self, edges):
        for start, end in edges:
            self.vertices[start].neighbors.append(self.vertices[end])

    def __str__(self):
        s = "Vertices - " + ''.join([" "+str(v.val) for v in self.vertices])
        for v in self.vertices:
            s += "\n" + str(v.val) + ":" + "".join([str(n.val)+"," for n in v.neighbors])
        return s
def shortest_path(start, end):

    backrefs = {}
    queue = []
    backrefs[start] = None
    queue.insert(0, start)
    while queue:
        v = queue.pop()
        if v == end:
            break

        for n in v.neighbors:
            if n in backrefs:
                continue
            backrefs[n] = v
            queue.insert(0, n)

    if v not in backrefs:
        return None

    path = []
    v = end
    while backrefs[v] is not None:
        path += v.val
        v = backrefs[v]

    return path.reverse()

def test():
    g = DiGraph(3, [(0,2),(1,2),(2,0),(2,1),(1,0)])
    print(g)

if __name__ == "__main__":
    test()

