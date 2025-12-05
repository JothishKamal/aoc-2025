def solve():
    with open("input.txt") as f:
        ranges = []
        for line in f:
            if line.__contains__("-"):
                parts = line.strip().split("-")
                ranges.append((int(parts[0]), int(parts[1])))

        ranges.sort()
        curr = -1
        fresh = 0
        for s, e in ranges:
            if curr >= s:
                s = curr + 1
            if e >= s:
                fresh += e - s + 1
                curr = max(curr, e)

        print(fresh)


if __name__ == "__main__":
    solve()
