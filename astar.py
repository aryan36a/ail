import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goalIndex = goal.index(tile)

            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goalIndex, 3)

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


# Generate possible moves
def getMoves(state):
    moves = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            newBlank = nr * 3 + nc

            newState = list(state)

            newState[blank], newState[newBlank] = (
                newState[newBlank],
                newState[blank]
            )

            moves.append(tuple(newState))

    return moves


# A* Search
def astar(start, goal):
    pq = []

    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for newState in getMoves(state):
            if newState not in visited:
                newG = g + 1
                newF = newG + heuristic(newState)

                heapq.heappush(
                    pq,
                    (newF, newG, newState, path + [newState])
                )

    return None


# Print solution
def printState(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


ans = astar(start, goal)

if ans:
    for step, state in enumerate(ans):
        print("Step:", step)
        printState(state)
else:
    print("No solution")