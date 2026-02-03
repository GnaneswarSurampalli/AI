from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E'],
    'C': ['D', 'E', 'F'],
    'D': ['E', 'F', 'G'],
    'E': ['F', 'G'],
    'F': ['G', 'H', 'I'],
    'G': ['H', 'I', 'J'],
    'H': ['I', 'J'],
    'I': ['J'],
    'J': ['K'],
    'K': ['L'],
    'L': ['M'],
    'M': []
}

start = 'A'
goal = 'M'

queue = deque([start])
visited = []
parent = {start: None} 
step = 1
print("Basic BFS\n")
print("\nDRY RUN TABLE (BFS)\n")
print(f"{'Step':<5}{'Queue':<25}{'Current':<12}{'Visited':<62}{'Parent Update'}")
print("-"*120)

while queue:
    current = queue.popleft()

    if current not in visited:
        visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current

                print(f"{step:<5}{str(list(queue)):<25}{current:<12}{str(visited):<65}{neighbor} ← {current}")
                step += 1

    if current == goal:
        break

path = []
node = goal
while node:
    path.append(node)
    node = parent[node]

path.reverse()

print("\nShortest Path:")
print(" -> ".join(path))