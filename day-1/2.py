def solve():
    pos = 50
    ct = 0

    with open("input.txt") as f:
        for line in f:
            dir = line[0]
            dist = int(line[1:])

            if dir == "L":
                if dist >= pos and pos > 0:
                    rem = dist - pos
                    ct += 1 + rem // 100
                elif pos == 0 and dist > 0:
                    ct += dist // 100

                pos = (pos - dist) % 100

            elif dir == "R":
                clicks = 100 - pos
                if dist >= clicks:
                    rem = dist - clicks
                    ct += 1 + rem // 100

                pos = (pos + dist) % 100

    print(ct)


if __name__ == "__main__":
    solve()
