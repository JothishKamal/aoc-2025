def solve():
    pos = 50
    ct = 0
    with open("input.txt") as f:
        for line in f:
            dir = line[0]
            dist = int(line[1:])

            if dir == "L":
                pos = (pos - dist) % 100
            elif dir == "R":
                pos = (pos + dist) % 100

            if pos == 0:
                ct += 1

    print(ct)


if __name__ == "__main__":
    solve()
