def hill_climbing(graph, start, goal):
    current = start
    path = [current]
    
    while current != goal:
        print(f"Current Node: {current}, h(n): {heuristic[current]}")
        
        neighbors = graph[current]
        
        print("All Neighbors:")
        for n in neighbors:
            print(f"h({n}):{heuristic[n]}")
            
        best_neighbor = min(neighbors, key=lambda x: heuristic[x])
        
        print(f"Best Neighbor: {best_neighbor}, h(n): {heuristic[best_neighbor]}")
        
        if heuristic[best_neighbor] >= heuristic[current]:
            print("Terminating, no better neighbors.")
            break
        
        current = best_neighbor
        path.append(current)

    return path

graph = {
    'A': ['B', 'C', 'U'],
    'B': ['E', 'G'],
    'C': ['G', 'I', 'J'],
    'U': ['K', 'Y'],
    'E': ['G', 'M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K'],
    'K': ['J'],
    'Y': ['M']
}

heuristic = {
    'A': 7, 'B': 5, 'C': 3, 'U': 4, 'E': 2, 
    'G': 3, 'I': 6, 'J': 4, 'K': 1, 'Y': 2, 'M': 0
}

path = hill_climbing(graph, 'A', 'M')
print(f"The final path Hill Climbing went through: {' -> '.join(path)}")
