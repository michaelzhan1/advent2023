from collections import defaultdict


fname = '16.in'


def part1():
    with open(fname) as f:
        grid = [list(line.strip()) for line in f.readlines()]
    n = len(grid)
    m = len(grid[0])

    energized = set()
    visited = set()
    stack = []
    stack.append((0, 0, 'right'))
    while stack:
        i, j, direction = stack.pop()
        if (i, j, direction) in visited:
            continue
        visited.add((i, j, direction))
        energized.add((i, j))

        new_directions = []
        obj = grid[i][j]
        if obj == '-':
            if direction == 'right' or direction == 'left':
                new_directions.append(direction)
            else:
                new_directions.append('left')
                new_directions.append('right')
        elif obj == '|':
            if direction == 'up' or direction == 'down':
                new_directions.append(direction)
            else:
                new_directions.append('up')
                new_directions.append('down')
        elif obj == '/':
            if direction == 'right':
                new_directions.append('up')
            elif direction == 'up':
                new_directions.append('right')
            elif direction == 'left':
                new_directions.append('down')
            elif direction == 'down':
                new_directions.append('left')
        elif obj == '\\':
            if direction == 'right':
                new_directions.append('down')
            elif direction == 'down':
                new_directions.append('right')
            elif direction == 'left':
                new_directions.append('up')
            elif direction == 'up':
                new_directions.append('left')
        elif obj == '.':
            new_directions.append(direction)
        
        for new_direction in new_directions:
            if new_direction == 'right':
                next_i = i
                next_j = j + 1
            elif new_direction == 'up':
                next_i = i - 1
                next_j = j
            elif new_direction == 'left':
                next_i = i
                next_j = j - 1
            elif new_direction == 'down':
                next_i = i + 1
                next_j = j
                
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue
            stack.append((next_i, next_j, new_direction))    
    print(len(energized))
    

def part2():
    with open(fname) as f:
        grid = [list(line.strip()) for line in f.readlines()]
    n = len(grid)
    m = len(grid[0])

    def get_energized(start_i, start_j, start_direction):
        energized = set()
        visited = set()
        stack = []
        stack.append((start_i, start_j, start_direction))
        while stack:
            i, j, direction = stack.pop()
            if (i, j, direction) in visited:
                continue
            visited.add((i, j, direction))
            energized.add((i, j))

            new_directions = []
            obj = grid[i][j]
            if obj == '-':
                if direction == 'right' or direction == 'left':
                    new_directions.append(direction)
                else:
                    new_directions.append('left')
                    new_directions.append('right')
            elif obj == '|':
                if direction == 'up' or direction == 'down':
                    new_directions.append(direction)
                else:
                    new_directions.append('up')
                    new_directions.append('down')
            elif obj == '/':
                if direction == 'right':
                    new_directions.append('up')
                elif direction == 'up':
                    new_directions.append('right')
                elif direction == 'left':
                    new_directions.append('down')
                elif direction == 'down':
                    new_directions.append('left')
            elif obj == '\\':
                if direction == 'right':
                    new_directions.append('down')
                elif direction == 'down':
                    new_directions.append('right')
                elif direction == 'left':
                    new_directions.append('up')
                elif direction == 'up':
                    new_directions.append('left')
            elif obj == '.':
                new_directions.append(direction)
            
            for new_direction in new_directions:
                if new_direction == 'right':
                    next_i = i
                    next_j = j + 1
                elif new_direction == 'up':
                    next_i = i - 1
                    next_j = j
                elif new_direction == 'left':
                    next_i = i
                    next_j = j - 1
                elif new_direction == 'down':
                    next_i = i + 1
                    next_j = j
                    
                if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                    continue
                stack.append((next_i, next_j, new_direction))    
        return len(energized)

    res = 0
    for i in range(n):
        res = max(res, get_energized(i, 0, 'right'))
        res = max(res, get_energized(i, m - 1, 'left'))
    
    for j in range(m):
        res = max(res, get_energized(0, j, 'down'))
        res = max(res, get_energized(n - 1, j, 'up'))
    
    print(res)


if __name__ == '__main__':
    part1()
    part2()
