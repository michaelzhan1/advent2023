fname = 'test.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    lines = all_lines.strip().split('\n')
    lines = list(line.split() for line in lines)
    n = len(lines)
    for i in range(n):
        lines[i][1] = int(lines[i][1])
    
    for line in lines:
        print(line)


def part2():
    with open(fname) as f:
        all_lines = f.read()


if __name__ == "__main__":
    part1()
    part2()
