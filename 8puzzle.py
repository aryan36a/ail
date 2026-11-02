from collections import deque
start=(1,2,3,
       4,0,6,
       7,5,8)

goal=(1,2,3,
      4,5,6,
      7,8,0)

def getMoves(state):
    moves=[]

    blankIdx=state.index(0)

    blankRow=blankIdx//3
    blankCol=blankIdx%3

    directions=[
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    for dr,dc in directions:
        nr=blankRow+dr
        nc=blankCol+dc

        if 0<=nr<3 and 0<=nc<3:
            newBlankIdx=3*nr+nc
            newState=list(state)

            newState[newBlankIdx],newState[blankIdx]=(newState[blankIdx],newState[newBlankIdx])

            moves.append(tuple(newState))
    return moves


def bfs(start,goal):
    queue=deque([(start,[])])

    visited={start}

    while queue:
        state,path=queue.popleft()

        if state==goal:
            return path+[state]

        for newState in getMoves(state):
            if newState not in visited:
                visited.add(newState)
                queue.append((newState,path+[newState]))

    return None

ans=bfs(start,goal)
x=0
for i in range(len(ans)):
    if x%3==0:
        print(end="\n")
        print(ans[i]) 
    else:
        print(ans[i])
        x+=1