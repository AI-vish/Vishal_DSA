from collections import defaultdict

class Graph:
    def __init__(self):
        # Use defaultdict to store the graph
        self.adjacency_list = defaultdict(list)

    def add_edge(self, start, end):
        # Function to add an edge to the graph
        self.adjacency_list[start].append(end)

    def depth_first_search_util(self, vertex, visited):
        # Utility function for DFS traversal
        visited.add(vertex)
        print(vertex, end=' ')

        # Recursive call for adjacent vertices
        for neighbour in self.adjacency_list[vertex]:
            if neighbour not in visited:
                self.depth_first_search_util(neighbour, visited)

    def depth_first_search(self, start_vertex):
        # Function for DFS traversal
        visited = set()
        self.depth_first_search_util(start_vertex, visited)


# Driver code
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Depth First Traversal starting from vertex 2:")
    
    # Function call for DFS traversal
    graph.depth_first_search(2)
