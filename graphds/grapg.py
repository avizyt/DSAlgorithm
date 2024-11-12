class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertext(self, vertext):
        if vertext not in self.adjacency_list:
            self.adjacency_list[vertext] = []

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)


class Algorithms(Graph):
    def __init__(self) -> None:
        super().__init__()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graph()
for v in range(1, 6):
    g.add_vertext(v)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print("Depth-First Search starting from vertex 1:")
algo = Algorithms()
algo.dfs(2)
