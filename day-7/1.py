from collections import deque


def solve():
    with open("input.txt") as f:
        D = f.read()

    G = [list(row) for row in D.splitlines()]
    R = len(G)
    C = len(G[0])

    sr, sc = 0, 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == "S":
                sr, sc = r, c
                break

    split = 0
    dq = deque([(sr, sc)])
    seen = set()
    while dq:
        r, c = dq.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if r + 1 == R:
            continue
        if G[r + 1][c] == "^":
            dq.append((r + 1, c - 1))
            dq.append((r + 1, c + 1))
            split += 1
        else:
            dq.append((r + 1, c))

    print(split)


if __name__ == "__main__":
    solve()
