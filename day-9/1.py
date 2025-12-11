from math import dist


def solve():
    points = []
    with open("input.txt") as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))

    res = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            if area > res:
                res = area

    print(res)


if __name__ == "__main__":
    solve()
