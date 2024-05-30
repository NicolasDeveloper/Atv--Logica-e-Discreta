import heapq

def prim(graph):
    # Inicial aqui
    visited = set()
    mst = []
    start_node = list(graph.keys())[0]
    visited.add(start_node)
    neighbor: object
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            for neighbor, cost in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, v, neighbor))

    return mst


# Exemplo de teste:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst_prim = prim(graph)
print("MST usando o algoritmo de Prim:", mst_prim)
