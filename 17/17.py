import heapq


fname = '17.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    grid = [list(map(int, line)) for line in all_lines.strip().split('\n')]
    n = len(grid)
    m = len(grid[0])

    all_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def astar(i, j, direction):
        pq = []

        heapq.heappush(pq, (0, i, j, direction))
        visited = set()
        while pq:
            distance, i, j, direction = heapq.heappop(pq)
            if i == n - 1 and j == m - 1:
                return distance
            if (i, j, direction) in visited:
                continue
            visited.add((i, j, direction))
            
            for dx, dy in all_directions:
                if (dx, dy) == direction or (-dx, dy) == direction or (dx, -dy) == direction:
                    continue
                running_total = distance
                for k in range(1, 4):
                    x = i + k * dx
                    y = j + k * dy
                    if x < 0 or x >= n or y < 0 or y >= m:
                        break
                    running_total += grid[x][y]
                    if (x, y, (dx, dy)) not in visited:
                        heapq.heappush(pq, (running_total, x, y, (dx, dy)))
        return -1
    print(min(astar(0, 0, (1, 0)), astar(0, 0, (0, 1))))


def part2():
    with open(fname) as f:
        all_lines = f.read()
    grid = [list(map(int, line)) for line in all_lines.strip().split('\n')]
    n = len(grid)
    m = len(grid[0])

    all_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def astar(i, j, direction):
        pq = []

        heapq.heappush(pq, (0, i, j, direction))
        visited = set()
        while pq:
            distance, i, j, direction = heapq.heappop(pq)
            if i == n - 1 and j == m - 1:
                return distance
            if (i, j, direction) in visited:
                continue
            visited.add((i, j, direction))
            
            for dx, dy in all_directions:
                if (dx, dy) == direction or (-dx, dy) == direction or (dx, -dy) == direction:
                    continue
                for k in range(4, 11):
                    x = i + k * dx
                    y = j + k * dy
                    if x < 0 or x >= n or y < 0 or y >= m:
                        break
                    new_distance = distance
                    if dx == 1:
                        new_distance += sum(grid[i + ii][j] for ii in range(1, k + 1))
                    elif dy == 1:
                        new_distance += sum(grid[i][j + ii] for ii in range(1, k + 1))
                    elif dx == -1:
                        new_distance += sum(grid[i - ii][j] for ii in range(1, k + 1))
                    elif dy == -1:
                        new_distance += sum(grid[i][j - ii] for ii in range(1, k + 1))



                    if (x, y, (dx, dy)) not in visited:
                        heapq.heappush(pq, (new_distance, x, y, (dx, dy)))
        return -1
    print(min(astar(0, 0, (1, 0)), astar(0, 0, (0, 1))))


if __name__ == "__main__":
    part1()
    part2()
