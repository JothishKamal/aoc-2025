def count(grid, r, c):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    ct = 0
    rows = len(grid)
    cols = len(grid[0])

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                ct += 1
    return ct


def solve():
    grid = []
    with open("input.txt") as f:
        for line in f:
            grid.append(line.strip())

    rows = len(grid)
    cols = len(grid[0])
    ct = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                adj = count(grid, r, c)
                if adj < 4:
                    ct += 1

    print(ct)


if __name__ == "__main__":
    solve()
