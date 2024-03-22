import heapq

def heuristic(node):
    return Heuristics.get(node, float('inf'))

def a_star(start, goal):
    
    open_list = [(heuristic(start), start)]  # Priority queue (f-value, node)
    g_values = {node: float('inf') for node in Graph}
    g_values[start] = 0
    parents = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for neighbor, distance in Graph[current]:
            tentative_g = g_values[current] + distance
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_value, neighbor))
                parents[neighbor] = current

    return None  # No path found

def get_input_from_user():
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        city1, city2, distance = input("Enter city1 city2 distance: ").split()
        distance = int(distance)
        if city1 not in Graph:
            Graph[city1] = []
        if city2 not in Graph:
            Graph[city2] = []
        Graph[city1].append((city2, distance))
        # Graph_nodes[city2].append((city1, distance))

    for node in Graph:
        heuristic_value = int(input(f"Enter heuristic value for node {node}: "))
        Heuristics[node] = heuristic_value

# Define the graph and heuristic values
Graph = {}
Heuristics = {}

if __name__ == "__main__":
    get_input_from_user()
    start_node = input("Enter the start node: ")
    stop_node = input("Enter the destination node: ")
    path = a_star(start_node, stop_node)
    print("Shortest path:", path)
