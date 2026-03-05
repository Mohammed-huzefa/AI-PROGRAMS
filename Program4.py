import heapq

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def parse_graph_input():
    graph = {}
    num_edges = int(input("Enter number of edges: "))

    for _ in range(num_edges):
        u, v, cost = input("Enter edge (u v cost): ").split()
        cost = int(cost)

        if u not in graph:
            graph[u] = []

        graph[u].append((v, cost))

    return graph


def heuristic(node):
    h = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 1,
        'E': 2,
        'G': 0
    }
    return h.get(node, 0)


def ao_star(start, goal, graph):

    open_list = []
    heapq.heappush(open_list, (heuristic(start), Node(start)))

    visited = set()

    while open_list:

        _, current = heapq.heappop(open_list)

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        visited.add(current.state)

        for neighbor, cost in graph.get(current.state, []):

            if neighbor not in visited:
                new_cost = cost + heuristic(neighbor)
                new_node = Node(neighbor, current, new_cost)
                heapq.heappush(open_list, (new_cost, new_node))

    return None


if __name__ == "__main__":

    print("Define Graph")
    graph = parse_graph_input()

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    result = ao_star(start, goal, graph)

    if result:
        print("Path found:")
        for node in result:
            print(node, end=" ")
    else:
        print("No path found")