def solve():
    with open("input.txt") as f:
        line = f.readline().strip()
        ranges = line.split(",")

        invalids = []
        for r in ranges:
            a, b = map(int, r.split("-"))

            for i in range(a, b + 1):
                str_i = str(i)
                length = len(str_i)

                if length % 2 == 0:
                    mid = length // 2
                    left = str_i[:mid]
                    right = str_i[mid:]
                    if left == right:
                        invalids.append(i)
                else:
                    continue

        sum = 0
        for inv in invalids:
            sum += int(inv)

        print(sum)


if __name__ == "__main__":
    solve()
