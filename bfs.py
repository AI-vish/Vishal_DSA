def bfs(graph, start):
    visited = set()
    visited.add(start)
    next_level = [start]

    while next_level:
        current_level = next_level
        next_level = []

        for node in current_level:
            # Process node here or perform any desired operation

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)

# Test Case
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

bfs(graph, 'A')
