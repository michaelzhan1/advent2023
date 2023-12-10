from collections import deque
import os


def part1():
    res = 0

    # 0 = left, 1 = up, 2 = right, 3 = down
    slots = {
        'F': [False, False, True, True],
        'L': [False, True, True, False],
        '7': [True, False, False, True],
        'J': [True, True, False, False],
        '|': [False, True, False, True],
        '-': [True, False, True, False],
    }

    grid = []
    with open('10.in') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                si, sj = i, j

    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    queue = deque()
    queue.append((si, sj))
    seen = set()
    seen.add((si, sj))
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            if grid[i][j] == 'S':
                for dx, dy in direction:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] != '.':
                        if (x, y) not in seen and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
                            queue.append((x, y))
                            seen.add((x, y))
            else:
                for idx in range(4):
                    if slots[grid[i][j]][idx]:
                        dx, dy = direction[idx]
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and grid[x][y] != '.':
                            if (x, y) not in seen and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
                                queue.append((x, y))
                                seen.add((x, y))
        res += 1
    print(res - 1)
            

def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
