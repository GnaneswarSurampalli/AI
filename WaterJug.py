jug1, jug2, goal = 4, 3, 2

visited = [[False for _ in range(jug2 + 1)] for _ in range(jug1 + 1)]
steps = []

def waterJug(x, y):
    if visited[x][y]:
        return False

    visited[x][y] = True
    steps.append((x, y))

    if (x == goal and y == 0) or (y == goal and x == 0):
        return True

    if (waterJug(0, y) or
        waterJug(x, 0) or
        waterJug(jug1, y) or
        waterJug(x, jug2) or
        waterJug(x + min(y, jug1 - x), y - min(y, jug1 - x)) or
        waterJug(x - min(x, jug2 - y), y + min(x, jug2 - y))):
        return True

    steps.pop()
    return False


if waterJug(0, 0):
    print("Steps:")
    print("Jug1\tJug2")
    print("-----\t-----")
    for s in steps:
        print(s[0], "\t", s[1])
    print("Solution Found")
else:
    print("No solution")
