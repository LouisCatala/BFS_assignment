from queue import PriorityQueue

def a_star_search(graph, start, goal):
    g_score = {start: 0}  # G(n)
    f_score = {start: 0}  # F(n)
    open_set = PriorityQueue()
    open_set.put((10, 0, 0, start))  # f_score(set to 10 bc heuristic), -g_score, counter, node
    came_from = {}
    counter = 0  # keep track of when nodes were added
    step = 1  # Use to list steps for output
    while not open_set.empty():
        print(f"Step {step}")
        step += 1
        current_f_score, _, _, current = open_set.get()

        print(f"Current: {current}, f(n): {current_f_score}")  # Print current node and f_score

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor in graph[current].keys():
            tentative_g_score = g_score[current] + graph[current][neighbor]['cost']

            print(f"Chosen Neignbor: {neighbor}")   

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + graph[current][neighbor]['heuristic']

                counter += 1  # Increase counter for the next node
                open_set.put((f_score[neighbor], -g_score[neighbor], counter, neighbor))

                print(f" Neighbor Added to set: {neighbor}, f(n): {f_score[neighbor]}")  # Print node added to open set

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

graph = {
    'S': {'A': {'cost': 3, 'heuristic': 8}, 'B': {'cost': 2, 'heuristic': 9}, 'C': {'cost': 5, 'heuristic': 7}},
    'A': {'G': {'cost': 2, 'heuristic': 6}},
    'B': {'D': {'cost': 6, 'heuristic': 4}},
    'C': {'H': {'cost': 3, 'heuristic': 6}},
    'D': {'F': {'cost': 3, 'heuristic': 0}},
    'G': {'E': {'cost': 5, 'heuristic': 3}},
    'E': {'F': {'cost': 1, 'heuristic': 0}},
    'H': {'F': {'cost': 2, 'heuristic': 0}}
}

if __name__ == "__main__":
    path, cost = a_star_search(graph, 'S', 'F')
    print(f"The shortest path is {path}")
    print(f"The actual cost is {cost} units.")