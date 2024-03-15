from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start, end):
        visited = []
        queue = []
        path = []

        queue.append(start)
        visited.append(start)

        while queue:
            s = queue.pop(0)
            path.append(s)

            if s == end:
                return path

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

    def dfs_util(self, node, visited, end, path):
        visited.append(node)
        path.append(node)

        if node == end:
            return path

        for i in self.graph[node]:
            if i not in visited:
                newPath =  self.dfs_util(i, visited, end, path)
                if newPath:
                    return newPath

    def dfs(self, start, end):
        visited = []
        path = []
        return self.dfs_util(start, visited, end, path)


if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start_node = int(input("Enter the source node: "))
    end_node = int(input("Enter the destination node: "))

    print("BFS path:", g.bfs(start_node, end_node))
    print("DFS path:", g.dfs(start_node, end_node))
