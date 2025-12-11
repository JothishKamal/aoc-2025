from functools import cache


def solve():
    G = {}

    with open("input.txt") as f:
        for line in f:
            a, b = line.strip().split(": ")
            G[a] = b.split()

    @cache
    def dfs(u, seen_dac, seen_fft):
        seen_dac |= u == "dac"
        seen_fft |= u == "fft"

        if u == "out":
            return 1 if (seen_dac and seen_fft) else 0

        total = 0
        for v in G.get(u, []):
            total += dfs(v, seen_dac, seen_fft)
        return total

    print(dfs("svr", False, False))


if __name__ == "__main__":
    solve()
