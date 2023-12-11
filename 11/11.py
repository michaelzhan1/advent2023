from bisect import bisect_left


fname = '11.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    matrix = all_lines.split('\n')
    matrix = [list(row) for row in matrix]
    empty_rows = []
    empty_cols = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if all([matrix[i][j] == '.' for j in range(m)]):
            empty_rows.append(i)
    
    for j in range(m):
        if all([matrix[i][j] == '.' for i in range(n)]):
            empty_cols.append(j)
    
    for i in reversed(empty_rows):
        matrix.insert(i, ['.' for _ in range(m)])

    for j in reversed(empty_cols):
        for i in range(len(matrix)):
            matrix[i].insert(j, '.')

    n = len(matrix)
    m = len(matrix[0])
    
    galaxies = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                galaxies.append((i, j))
    
    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            res += abs(x1 - x2) + abs(y1 - y2)
    print(res)


def part2():
    with open(fname) as f:
        all_lines = f.read()
    matrix = all_lines.split('\n')
    matrix = [list(row) for row in matrix]
    empty_rows = []
    empty_cols = []

    factor = 1000000

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if all([matrix[i][j] == '.' for j in range(m)]):
            empty_rows.append(i)
    
    for j in range(m):
        if all([matrix[i][j] == '.' for i in range(n)]):
            empty_cols.append(j)

    # between any two galaxies, if there is an empty row or column, 
    # the path is extended by factor - 1

    galaxies = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                galaxies.append((i, j))
    
    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]

            x1_idx = bisect_left(empty_rows, x1)
            x2_idx = bisect_left(empty_rows, x2)

            y1_idx = bisect_left(empty_cols, y1)
            y2_idx = bisect_left(empty_cols, y2)

            res += abs(x1 - x2) + abs(x2_idx - x1_idx) * (factor - 1) + abs(y1 - y2) + abs(y2_idx - y1_idx) * (factor - 1)
    print(res)


if __name__ == '__main__':
    part1()
    part2()
