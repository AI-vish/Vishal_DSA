import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    total_distance = 0  # Initialize total_distance variable
    paths = {node: [] for node in graph}  # Initialize paths dictionary

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                paths[neighbor] = paths[current_node] + [current_node]

    shortest_paths = {}
    for node, path in paths.items():
        if node != start and distances[node] != float('inf'):
            shortest_paths[node] = [start] + path + [node]

    for node, dist in distances.items():
        if dist != float('inf'):  # Consider only the calculated distances
            total_distance += dist

    return distances, total_distance, shortest_paths  # Return distances, total_distance, and shortest_paths

# Test Case
graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {}
}

distances, total_distance, shortest_paths = dijkstra(graph, 'A')
print("Distances:", distances)  # Print the distances dictionary
print("Total Distance:", total_distance)  # Print the total distance sum
print("Shortest Paths:", shortest_paths)  # Print the shortest paths
