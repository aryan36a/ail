from collections import deque

grid = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS=len(grid)
COLS=len(grid[0])
start=(0,0)
end=(4,4)

internalMap={}
visited=set()
position=start
path=[start]


directions=[
    (-1,0),#UP
    (1,0),#DOWN
    (0,-1),#LEFT
    (0,1)#RIGHT
]

def perceive():
    r, c = position

    internalMap[(r, c)] = grid[r][c]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            internalMap[(nr, nc)] = grid[nr][nc]

def isValid(pos):
    r,c=pos

    if r<0 or r>=ROWS or c<0 or c>=COLS or internalMap.get(pos)=='#':
        return False
    return True

def bfs():
    queue = deque([(position, [position])])
    bfsVisited = {position}

    while queue:
        current, currentPath = queue.popleft()

        if current == end:
            return currentPath

        r, c = current

        for dr, dc in directions:
            nextPos = (r + dr, c + dc)

            if nextPos not in bfsVisited and isValid(nextPos):

                bfsVisited.add(nextPos)

                newPath = currentPath + [nextPos]

                queue.append((nextPos, newPath))

    return None
def selectAction(next_pos):
    r, c = position
    nr, nc = next_pos

    if nr == r - 1:
        return "UP"
    elif nr == r + 1:
        return "DOWN"
    elif nc == c - 1:
        return "LEFT"
    elif nc == c + 1:
        return "RIGHT"

    return "STOP"

def makeMove(nextPos):
    global position

    action=selectAction(nextPos)

    print("Current Position: ",position)
    print("Action: ",action)

    position=nextPos
    visited.add(position)
    path.append(position)

    print("New Position: ",nextPos)

def run():
    visited.add(position)

    while position!=end:
        perceive()

        result=bfs()

        if result is None:
            print("No path found")
            return
        if len(result)>0:
            makeMove(result[1])

    print("\nGoal Reached")
    print("Complete Path: ",path)
    print("Visited Positions: ",visited)

run()