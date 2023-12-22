from collections import deque


fname = '21.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    grid = list(map(list, all_lines.split('\n')))
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
                break

    MAX_STEPS = 64

    # bfs
    queue = deque()
    queue.append((start[0], start[1], 0))
    seen = set()
    seen.add((start[0], start[1], 0))
    steps = 0
    while queue:
        size = len(queue)
        if steps == MAX_STEPS:
            break
        for _ in range(size):
            i, j, distance = queue.popleft()
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != '#' and (x, y, distance + 1) not in seen:
                    seen.add((x, y, distance + 1))
                    queue.append((x, y, distance + 1))
        steps += 1

    print(len(queue))
        

def part2():
    with open(fname) as f:
        all_lines = f.read()
    grid = list(map(list, all_lines.split('\n')))
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
                break

    MAX_STEPS = 5000

    # bfs
    queue = deque()
    queue.append((start[0], start[1], 0))
    seen = set()
    seen.add((start[0], start[1], 0))
    steps = 0
    while queue:
        size = len(queue)
        if steps == MAX_STEPS:
            break
        for _ in range(size):
            i, j, distance = queue.popleft()
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != '#' and (x, y, distance + 1) not in seen:
                    seen.add((x, y, distance + 1))
                    queue.append((x, y, distance + 1))
        steps += 1

    print(len(queue))


if __name__ == '__main__':
    part1()
    part2()

