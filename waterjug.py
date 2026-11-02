
def dfs():
    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == 2 or b == 2:
            return path

        next_states = [
            (4, b),  # Fill Jug A
            (a, 3),  # Fill Jug B
            (0, b),  # Empty Jug A
            (a, 0),  # Empty Jug B
            (a - min(a, 3 - b), b + min(a, 3 - b)),  # A to B
            (a + min(b, 4 - a), b - min(b, 4 - a))   # B to A
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path))

    return None


result = dfs()

if result:
    print("Solution found:")
    for state in result:
        print(state)
else:
    print("No solution found")
