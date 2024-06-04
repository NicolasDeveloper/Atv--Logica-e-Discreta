class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and mst_set[v] is False:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [float('inf')] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Interface
def user_input():
    V = int(input("Digite o número de vértices: "))
    g = Graph(V)
    for i in range(V):
        for j in range(V):
            weight = int(input(f"Digite o peso da aresta entre o vértice {i} e o vértice {j} (0 se não houver aresta): "))
            g.graph[i][j] = weight
    return g

if __name__ == '__main__':
    g = user_input()
    parent = g.prim_mst()
    print_mst(parent, g.graph)
