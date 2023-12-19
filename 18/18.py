fname = '18.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    lines = all_lines.strip().split('\n')
    lines = list(line.split() for line in lines)
    n = len(lines)
    for i in range(n):
        lines[i][1] = int(lines[i][1])

    d_map = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    
    x = 0
    y = 0
    perimeter = 0
    area = 0
    for line in lines:
        d = d_map[line[0]]
        length = line[1]
        dy, dx = d
        y += dy * length
        x += dx * length
        perimeter += length
        area += x * dy * length
    print(area + perimeter // 2 + 1)


def part2():
    with open(fname) as f:
        all_lines = f.read()
    lines = all_lines.strip().split('\n')
    lines = list(line.split() for line in lines)
    n = len(lines)

    d_convert = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }

    for i in range(n):
        lines[i][0] = d_convert[lines[i][2][-2]]
        lines[i][1] = int(lines[i][2][2:-2], 16)

    d_map = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    
    x = 0
    y = 0
    perimeter = 0
    area = 0
    for line in lines:
        d = d_map[line[0]]
        length = line[1]
        dy, dx = d
        y += dy * length
        x += dx * length
        perimeter += length
        area += x * dy * length
    print(area + perimeter // 2 + 1)


if __name__ == "__main__":
    part1()
    part2()
