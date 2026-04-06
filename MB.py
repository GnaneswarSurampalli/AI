from queue import PriorityQueue

DOOR = 0
CENTER = 1

initial_state = (DOOR, CENTER, False, False)

def is_goal(state):
    return state[3] == True

def heuristic(state):
    monkey, box, on_box, has_banana = state
    if has_banana:
        return 0
    h = 0
    if monkey != box:
        h += 1
    if box != CENTER:
        h += 1
    if not on_box:
        h += 1
    return h

def get_successors(state):
    monkey, box, on_box, has_banana = state
    successors = []

    if has_banana:
        return []

    if monkey != box:
        successors.append(((box, box, False, False), "Move to Box"))

    if monkey == box and box != CENTER:
        successors.append(((CENTER, CENTER, False, False), "Push Box to Center"))

    if monkey == box and not on_box:
        successors.append(((monkey, box, True, False), "Climb Box"))

    if on_box and box == CENTER:
        successors.append(((monkey, box, True, True), "Grab Banana"))

    return successors

def a_star():
    pq = PriorityQueue()
    pq.put((heuristic(initial_state), 0, initial_state, []))
    visited = set()

    while not pq.empty():
        f, g, state, path = pq.get()

        if state in visited:
            continue
        visited.add(state)

        if is_goal(state):
            return path

        for next_state, action in get_successors(state):
            new_g = g + 1
            new_f = new_g + heuristic(next_state)
            pq.put((new_f, new_g, next_state, path + [action]))

    return None

solution = a_star()

if solution:
    print("Solution Found in Order:")
    for i, step in enumerate(solution, 1):
        print("Step", i, ":", step)
else:
    print("No Solution Found")
