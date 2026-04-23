import heapq

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == GOAL_STATE:
            return path + [current]

        visited.add(to_tuple(current))

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [current])
                )

    return None

def print_solution(solution):
    for step in solution:
        for row in step:
            print(row)
        print("------")

start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    print_solution(solution)
else:
    print("No solution exists.")

'''Experiment 5: Theory
Title:

Game Playing Algorithm (8 Puzzle Problem)

Theory:

The 8 Puzzle Problem is a classic problem in Artificial Intelligence used to demonstrate search and problem-solving techniques. It consists of a 3×3 grid with 8 numbered tiles and one empty space.

The objective is to rearrange the tiles from an initial state to a goal state by sliding tiles into the empty space.

The problem is solved using search algorithms such as:

Breadth First Search (BFS)
Depth First Search (DFS)
A* Algorithm

It is represented using:

Initial State: Starting arrangement of tiles
Goal State: Desired arrangement
Operators: Moves (up, down, left, right)

The solution involves exploring possible states until the goal state is reached.

Conclusion:

The 8 puzzle problem helps in understanding state space search and how AI algorithms find optimal solutions.'''