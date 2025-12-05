def solve():
    with open("input.txt") as f:
        ranges = []
        fresh = 0
        for line in f:
            if line.__contains__("-"):
                parts = line.strip().split("-")
                ranges.append((int(parts[0]), int(parts[1])))
            elif line.strip() == "":
                continue
            else:
                val = int(line.strip())
                for r in ranges:
                    if r[0] <= val <= r[1]:
                        fresh += 1
                        break

        print(fresh)


if __name__ == "__main__":
    solve()
