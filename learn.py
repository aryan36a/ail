#a=4
#b=3
#goal=2

def dfs():
    stack=[((0,0),[])]
    visited=set()

    while stack:
        (a,b),path=stack.pop()

        if(a,b) in visited:
            continue
        visited.add((a,b))

        path=path+[(a,b)]

        if a==2 or b==2:
            return path

        nextStates=[
            (4,b),
            (a,3),
            (0,b),
            (a,0),
            (a+min(b,4-a),b-min(b,4-a)),
            (a-min(a,3-b),b+min(a,3-b))
        ]

        for state in nextStates:
            if state not in visited:
                stack.append((state,path))
    return None

if dfs():
    print(dfs())