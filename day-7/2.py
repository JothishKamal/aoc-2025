from collections import deque
from functools import cache


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

    @cache
    def score(r, c):
        if r + 1 == R:
            return 1
        if G[r + 1][c] == "^":
            return score(r + 1, c - 1) + score(r + 1, c + 1)
        else:
            return score(r + 1, c)

    split = score(sr, sc)
    print(split)


if __name__ == "__main__":
    solve()
