import heapq

def a_star_search(graph, start, end, heuristic):
    open_set = [(heuristic[start], start)]
    came_from = {}
    g_costs = {start: 0}

    while open_set:
        print(f"Open set: {open_set}")

        _, current = heapq.heappop(open_set)
        print(f"Current path: {current}")
        print(f"Neighbor paths: {list(graph[current].keys())}")

        if current == end:
            path = []
            while current:
                path.insert(0, current)
                current = came_from.get(current)
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_cost = g_costs[current] + cost
            f_cost = tentative_g_cost + heuristic[neighbor]  # Sum of real distance and heuristic

            print(f"F(n) cost to {neighbor} path: {f_cost} (G(n): {tentative_g_cost}, H(n): {heuristic[neighbor]})")

            if tentative_g_cost < g_costs.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_costs[neighbor] = tentative_g_cost
                heapq.heappush(open_set, (f_cost, neighbor))

        print("----")

graph = {
    'S': {'A': 3, 'B': 2, 'C': 5},
    'A': {'G': 2, 'C': 3},
    'B': {'A': 4, 'D': 6},
    'C': {'B': 4, 'H': 3},
    'D': {'E': 2, 'F': 3},
    'E': {'F': 5},
    'F': {},
    'G': {'D': 4, 'E': 5},
    'H': {'A': 4, 'D': 4}
}

heuristic = {'S': 10, 'A': 8, 'B': 9, 'C': 7, 'D': 4, 'E': 3, 'F': 0, 'G': 6, 'H': 6}

result = a_star_search(graph, 'S', 'F', heuristic)
print(f"The shortest path is {result}")
