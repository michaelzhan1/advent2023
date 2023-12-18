from functools import cache


fname = 'test.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    grid = [list(map(int, line)) for line in all_lines.strip().split('\n')]
    n = len(grid)
    m = len(grid[0])

    # dijkstra
    

def part2():
    with open(fname) as f:
        all_lines = f.read()


if __name__ == "__main__":
    part1()
    part2()
