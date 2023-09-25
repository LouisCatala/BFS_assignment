from collections import deque

def bfs(start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        print(f"Queue: {list(queue)}")
        print(f"Visited: {visited}")

        current = queue.popleft()
        print(f"Current Node: {current}")

        if current == goal:
            print("Goal reached!")
            return

        visited.add(current)

        left_child = 2 * current
        right_child = (2 * current) + 1

        if left_child not in visited:
            queue.append(left_child)
            visited.add(left_child)

        if right_child not in visited:
            queue.append(right_child)
            visited.add(right_child)

        print("----")

if __name__ == "__main__":
    bfs(1, 11)
