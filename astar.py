from copy import deepcopy
from ast import literal_eval


def print_board(state):
    for r in state:
        print(*r)
    print()


def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c
    raise ValueError("Blank tile not found")


def heuristic(state, goal):
    f = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != 0 and state[r][c] != goal[r][c]:
                f += 1
    return f


def transition(cur, direction):
    r, c = find_blank(cur)
    new_state = deepcopy(cur)

    if direction == "up" and r > 0:
        new_state[r][c], new_state[r - 1][c] = new_state[r - 1][c], new_state[r][c]

    elif direction == "down" and r < 2:
        new_state[r][c], new_state[r + 1][c] = new_state[r + 1][c], new_state[r][c]

    elif direction == "left" and c > 0:
        new_state[r][c], new_state[r][c - 1] = new_state[r][c - 1], new_state[r][c]

    elif direction == "right" and c < 2:
        new_state[r][c], new_state[r][c + 1] = new_state[r][c + 1], new_state[r][c]

    else:
        return None

    return new_state


def astar(initial, goal):
    OPEN = [[heuristic(initial, goal), 0, initial]]
    visited_cost = {str(initial): 0}
    parent_map = {str(initial): (None, None)}

    while OPEN:
        OPEN.sort()
        f, g, current = OPEN.pop(0)

        if current == goal:
            print("Path Found:\n")

            path = []
            moves = []
            key = str(current)

            while True:
                parent, move = parent_map[key]
                path.append(literal_eval(key))
                moves.append(move)
                if parent is None:
                    break
                key = str(parent)

            path.reverse()
            moves.reverse()
            moves = moves[1:]

            print("Directions:")
            print(" -> ".join(moves) if moves else "Already at goal")

            print("\nTransitions:")
            for s in path:
                print_board(s)

            return

        for direction in ["up", "down", "left", "right"]:
            successor = transition(current, direction)
            if successor is None:
                continue

            key = str(successor)
            new_g = g + 1

            if key not in visited_cost or new_g < visited_cost[key]:
                visited_cost[key] = new_g
                new_f = new_g + heuristic(successor, goal)
                OPEN.append([new_f, new_g, successor])
                parent_map[key] = (current, direction) # type: ignore

    print("No solution found.")


# Initial and goal states
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

initial_state = [
   [1, 2, 3],
    [7, 8, 0],
    [4, 5, 6]
]

astar(initial_state, goal_state)
