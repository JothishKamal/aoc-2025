from functools import cache


def solve():
    G = {}

    with open("input.txt") as f:
        for line in f:
            a, b = line.strip().split(": ")
            G[a] = b.split()

    @cache
    def dfs(u):
        if u == "out":
            return 1

        total = 0
        for v in G.get(u, []):
            total += dfs(v)
        return total

    print(dfs("you"))


if __name__ == "__main__":
    solve()
