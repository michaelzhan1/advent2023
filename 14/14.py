fname = '14.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    grid = [list(line) for line in all_lines.split('\n')]
    n = len(grid)
    m = len(grid[0])
    res = 0
    for j in range(m):
        score = n
        for i in range(n):
            if grid[i][j] == 'O':
                res += score
                score -= 1
            elif grid[i][j] == '#':
                score = n - i - 1
    print(res)


def part2():
    with open(fname) as f:
        all_lines = f.read()
    grid = [list(line) for line in all_lines.split('\n')]
    n = len(grid)
    m = len(grid[0])

    def rotate():
        nonlocal grid
        new_grid = [['.'] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_grid[j][n - i - 1] = grid[i][j]
        grid = new_grid
    
    def tilt():
        # tilt board upwards, so 'O' rolls into '#'
        for j in range(m):
            for i in range(n):
                for i in range(n):
                    if grid[i][j] == 'O' and i > 0 and grid[i - 1][j] == '.':
                        grid[i][j] = '.'
                        grid[i - 1][j] = 'O'
    
    def score():
        ans = 0
        R = len(grid)
        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='O':
                    ans += len(grid)-r
        return ans

    t = 0
    seen = {}
    while t < 1000000000:
        t += 1
        for j in range(4):
            tilt()
            rotate()
        hash = tuple(tuple(row) for row in grid)
        if hash in seen:
            cycle = t - seen[hash]
            t += (1000000000 - t) // cycle * cycle
        seen[hash] = t
    print(score())
            
if __name__ == '__main__':
    part1()
    part2()
