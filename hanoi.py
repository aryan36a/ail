from collections import deque

def hanoi(n):
    start=(tuple(range(n,0,-1)),(),())
    end=((),(),tuple(range(n,0,-1)))

    queue=deque([(start,[])])
    visited={start}

    while queue:
        state,path=queue.popleft()

        if state==end:
            return path

        for i in range(3):
            if state[i]:
                disk=state[i][-1]

                for j in range(3):
                    if i!=j and (not state[j] or state[j][-1]>disk):
                        p=[list(x) for x in state]
                        p[i].pop()

                        p[j].append(disk)

                        new=tuple(tuple(x) for x in p)

                        if new not in visited:
                            visited.add(new)
                            queue.append((new,path+[f"Move disk:{disk} from rod {i} to {j}."]))


n=int(input("Enter the number of disks: "))

ans=hanoi(n)

for i in range(len(ans)):
    print(ans[i])

print("Total Moves: ",len(ans))