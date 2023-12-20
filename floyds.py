def floyd_warshall(graph):
    n = len(graph)
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        distances[i][i] = 0

    for u in graph:
        for v in graph[u]:
            distances[u][v] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

# Test Case
INF = float('inf')
graph = {
    0: {0: 0, 1: 3, 3: 7},
    1: {2: 1},
    2: {3: 2},
    3: {}
}

result = floyd_warshall(graph)
for row in result:
    print(row)
