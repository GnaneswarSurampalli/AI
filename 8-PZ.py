

import heapq

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0, "UP"),
         (1, 0, "DOWN"),
         (0, -1, "LEFT"),
         (0, 1, "RIGHT")]

def h(state):
    d = 0
    for i in range(3):
        for j in range(3):
            v = state[i][j]
            if v != 0:
                x = (v - 1) // 3
                y = (v - 1) % 3
                d += abs(i - x) + abs(j - y)
    return d

def blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def astar(start):
    pq = []
    heapq.heappush(pq, (h(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            for step, (move, s) in enumerate(path, 1):
                print("Step-", step, "Move:", move)
                for row in s:
                    print(row)
                print()
            print("Goal State Reached!")
            return

        visited.add(tuple(map(tuple, state)))
        x, y = blank(state)

        for dx, dy, move in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    heapq.heappush(
                        pq,
                        (g + 1 + h(new_state), g + 1, new_state, path + [(move, new_state)])
                    )

print("Enter initial puzzle (use 0 for blank):")
start = [list(map(int, input().split())) for _ in range(3)]
astar(start)
