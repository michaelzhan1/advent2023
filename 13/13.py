fname = '13.in'


def find_h_symmetry(pattern):
    for center in range(1, len(pattern)):
        i = 0
        while center - i - 1 >= 0 and center + i < len(pattern):
            if pattern[center - i - 1] != pattern[center + i]:
                break
            i += 1
        else:
            return center
    return 0


def find_v_symmetry(pattern):
    for center in range(1, len(pattern[0])):
        i = 0
        while center - i - 1 >= 0 and center + i < len(pattern[0]):
            if [row[center - i - 1] for row in pattern] != [row[center + i] for row in pattern]:
                break
            i += 1
        else:
            return center
    return 0


def part1():
    res = 0
    with open(fname) as f:
        all_lines = f.read()
    patterns = all_lines.split('\n\n')
    for pattern in patterns:
        pattern = pattern.split('\n')
        pattern = [list(row) for row in pattern]
        res += find_h_symmetry(pattern) * 100
        res += find_v_symmetry(pattern)
    print(res)


def levenshtein(s1, s2):
    count = 0
    for a1, a2 in zip(s1, s2):
        if a1 != a2:
            count += 1
    return count


def h_smudge(pattern):
    for center in range(1, len(pattern)):
        i = 0
        smudged = 0
        while center - i - 1 >= 0 and center + i < len(pattern):
            distance = levenshtein(pattern[center - i - 1], pattern[center + i])
            if distance > 1:
                break
            smudged += distance
            i += 1
        else:
            if smudged == 1:
                return center
    return 0


def v_smudge(pattern):
    for center in range(1, len(pattern[0])):
        i = 0
        smudged = 0
        while center - i - 1 >= 0 and center + i < len(pattern[0]):
            distance = levenshtein([row[center - i - 1] for row in pattern], [row[center + i] for row in pattern])
            if distance > 1:
                break
            smudged += distance
            i += 1
        else:
            if smudged == 1:
                return center
    return 0


def part2():
    res = 0
    with open(fname) as f:
        all_lines = f.read()
    patterns = all_lines.split('\n\n')
    for pattern in patterns:
        pattern = pattern.split('\n')
        pattern = [list(row) for row in pattern]
        res += h_smudge(pattern) * 100
        res += v_smudge(pattern)
    print(res)


if __name__ == '__main__':
    part1()
    part2()
