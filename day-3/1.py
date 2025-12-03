def solve():
    with open("input.txt") as f:
        total = 0
        for line in f:
            line = line.strip()

            max_joltage = 0
            for i in range(len(line)):
                for j in range(i + 1, len(line)):
                    joltage = int(line[i] + line[j])
                    max_joltage = max(max_joltage, joltage)

            total += max_joltage

        print(total)


if __name__ == "__main__":
    solve()
