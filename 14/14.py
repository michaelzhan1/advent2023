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


if __name__ == '__main__':
    part1()
    part2()
