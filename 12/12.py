from functools import lru_cache


fname = '12.in'


def count(line):
    row, nums = line.split()
    nums = list(map(int, nums.split(',')))

    def dfs(i, cur):
        if i == len(row):
            splits = [s for s in cur.split('.') if s]
            return list(map(len, splits)) == nums
        if row[i] != '?':
            return dfs(i+1, cur+row[i])
        else:
            return dfs(i+1, cur+'#') + dfs(i+1, cur+'.')
    
    return dfs(0, '')

def part1():
    with open(fname) as f:
        all_lines = f.read()
    lines = all_lines.strip().split('\n')
    res = 0
    for line in lines:
        res += count(line)
    print(res)


def part2():
    with open(fname) as f:
        all_lines = f.read()


if __name__ == "__main__":
    part1()
    part2()
