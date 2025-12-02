def is_invalid(num: str) -> bool:
    length = len(num)

    for plen in range(1, length // 2 + 1):
        if length % plen == 0:
            pattern = num[:plen]

            if pattern * (length // plen) == num:
                return True

    return False


def solve():
    with open("input.txt") as f:
        line = f.readline().strip()
        ranges = line.split(",")

        invalids = []
        for r in ranges:
            a, b = map(int, r.split("-"))

            for i in range(a, b + 1):
                if is_invalid(str(i)):
                    invalids.append(i)

        sum = 0
        for inv in invalids:
            sum += int(inv)

        print(sum)


if __name__ == "__main__":
    solve()
