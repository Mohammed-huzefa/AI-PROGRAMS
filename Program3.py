import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, h=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.h = h

    def __lt__(self, other):
        return (self.cost + self.h) < (other.cost + other.h)


def astar(start, goal, graph):

    frontier = []
    heapq.heappush(frontier, Node(start, None, 0, abs(ord(start)-ord(goal))))

    visited = set()

    while frontier:

        current = heapq.heappop(frontier)

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        visited.add(current.state)

        for neighbor, cost in graph.get(current.state, []):
            if neighbor not in visited:
                heapq.heappush(frontier,
                    Node(neighbor,current,current.cost+cost,abs(ord(neighbor)-ord(goal))))

    return None


print("Define the graph")
graph = {}

n = int(input("Enter number of edges: "))

for _ in range(n):
    u,v,c = input("Enter edge (u v cost): ").split()
    c = int(c)

    if u not in graph: graph[u] = []
    if v not in graph: graph[v] = []

    graph[u].append((v,c))
    graph[v].append((u,c))


start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = astar(start,goal,graph)

if path:
    print("Optimal path found:")
    for i in path:
        print(i,end=" ")
else:
    print("No path found")