class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])

    def union(self, set1, set2):
        self.parent[set1] = set2


def kruskal(graph):
    mst = []
    vertices = set([v for v in graph])
    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()

    ds = DisjointSet(vertices)

    for cost, u, v in edges:
        set1 = ds.find(u)
        set2 = ds.find(v)
        if set1 != set2:
            mst.append((u, v, cost))
            ds.union(set1, set2)

    return mst


# Exemplo:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 5},
    'C': {'A': 3, 'B': 4, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

mst_kruskal = kruskal(graph)
print("MST usando o algoritmo de Kruskal:", mst_kruskal)
