def solve():
    with open("input.txt") as f:
        G = [list(row) for row in f.read().splitlines()]
    R, C = len(G), len(G[0])

    sum = 0
    start = 0
    for cc in range(C + 1):
        blank = True
        if cc < C:
            for r in range(R):
                if G[r][cc] != " ":
                    blank = False
        if blank:
            op = G[R - 1][start]
            assert op in "+*", op
            res = 0 if op == "+" else 1
            for c in range(cc - 1, start - 1, -1):
                n = 0
                for r in range(R - 1):
                    if G[r][c] != " ":
                        n = n * 10 + int(G[r][c])
                if op == "+":
                    res += n
                else:
                    res *= n
            sum += res
            start = cc + 1

    print(sum)


if __name__ == "__main__":
    solve()
