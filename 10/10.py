from collections import deque, defaultdict

file = '10.in'
start_letter = ''

def part1():
    global start_letter
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
    with open(file) as f:
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
    path = set()
    prev = {
        (si, sj): None
    }
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            last = (i, j)
            if grid[i][j] == 'S':
                for dx, dy in direction:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] != '.':
                        if (x, y) not in seen and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
                            queue.append((x, y))
                            seen.add((x, y))
                            prev[(x, y)] = (i, j)
            else:
                for idx in range(4):
                    if slots[grid[i][j]][idx]:
                        dx, dy = direction[idx]
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and grid[x][y] != '.':
                            if (x, y) not in seen and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
                                queue.append((x, y))
                                seen.add((x, y))
                                prev[(x, y)] = (i, j)
                            elif (x, y) in queue and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
                                temp = (x, y)
                                while temp != (si, sj):
                                    path.add(temp)
                                    temp = prev[temp]
        while last:
            path.add(last)
            last = prev[last]
        res += 1
    
    start_directions = [False] * 4
    for dx, dy in direction:
        x, y = si + dx, sj + dy
        if (x, y) in path and ((dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy])):
            start_directions[direction.index((dx, dy))] = True
    for letter in slots:
        if slots[letter] == start_directions:
            start_letter = letter
            break
    print(res - 1)
            

def part2():
    slots = {
        'F': [False, False, True, True],
        'L': [False, True, True, False],
        '7': [True, False, False, True],
        'J': [True, True, False, False],
        '|': [False, True, False, True],
        '-': [True, False, True, False],
    }
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    grid = []
    with open(file) as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    graph = defaultdict(list)
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                si, sj = i, j
                grid[i][j] = start_letter
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            for dx, dy in direction:
                idx = direction.index((dx, dy))
                if not slots[grid[i][j]][idx]:
                    continue
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != '.':
                    if (dx and slots[grid[x][y]][2 - dx]) or (dy and slots[grid[x][y]][1 - dy]):
                        graph[(i, j)].append((x, y))
    
    path = set()
    prev = {}
    # use bfs to find loops in graph, and add elements of loop to path
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        seen = set()
        seen.add((i, j))
        prev[(i, j)] = None
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                last = (i, j)
                for x, y in graph[(i, j)]:
                    if (x, y) not in seen:
                        queue.append((x, y))
                        seen.add((x, y))
                        prev[(x, y)] = (i, j)
                    elif (x, y) in queue:
                        temp = (i, j)
                        while temp:
                            path.add(temp)
                            temp = prev[temp]
        while last:
            path.add(last)
            last = prev[last]
        return

    bfs(si, sj)

    # count all "." enclosed by path
    res = 0
    odd = False
    skip = ''
    for i in range(n):
        for j in range(m):
            if (i, j) in path:
                if grid[i][j] == skip:
                    skip = ''
                    continue
                elif grid[i][j] in '|7J':
                    skip = ''
                    odd = not odd
                elif grid[i][j] == 'F':
                    skip = 'J'
                    odd = not odd
                elif grid[i][j] == 'L':
                    skip = '7'
                    odd = not odd
            elif odd:
                skip = ''
                res += 1
    print(res)

if __name__ == "__main__":
    part1()
    part2()
