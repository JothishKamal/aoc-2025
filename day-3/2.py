dp = {}


def max_joltage(bank, pos, need):
    if need == 0:
        return 0

    key = (pos, need)
    if key in dp:
        return dp[key]

    max_val = 0
    for i in range(pos, len(bank) - need + 1):
        digit = int(bank[i])
        rem = max_joltage(bank, i + 1, need - 1)
        val = digit * (10 ** (need - 1)) + rem
        max_val = max(max_val, val)

    dp[key] = max_val
    return max_val


def solve():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            global dp
            dp = {}
            val = max_joltage(line, 0, 12)
            total += val
        print(total)


if __name__ == "__main__":
    solve()
