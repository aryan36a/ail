from collections import deque

grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start=(0,0)
goal=(3,3)

def bfs(start,goal):
    queue=deque([(start,[start])])
    visited={start}

    while queue:
        (r,c),path=queue.popleft()

        if(r,c)==goal:
            return path

        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        for dr,dc in directions:
            nr=r+dr
            nc=c+dc

            if 0<=nr<4 and 0<=nc<4:
                if grid[nr][nc]==0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append(((nr,nc),path+[(nr,nc)]))

    return None

path=bfs(start,goal)
if path:
    print("Path: ",path)
else:
    print("No Path Found")