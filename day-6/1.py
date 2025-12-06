def solve():
    with open("input.txt") as f:
        l = []
        for line in f:
            line = line.strip().split()
            l.append(line)

        m = len(l[0])
        n = len(l)

        sum = 0
        for i in range(m):
            flag = False if l[-1][i] == "+" else True

            res = 1 if flag else 0
            for j in range(n - 2, -1, -1):
                if flag:
                    res *= int(l[j][i])
                else:
                    res += int(l[j][i])

            sum += res

    print(sum)


if __name__ == "__main__":
    solve()
