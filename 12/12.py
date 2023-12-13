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

dp = {}
def get_score(row, nums, i, j, cur):
    key = (i, j, cur)
    if key in dp:
        return dp[key]
    if i == len(row):
        if (j == len(nums) and cur == 0) or (j == len(nums) - 1 and nums[-1] == cur):
            return 1
        else:
            return 0
    res = 0
    for choice in '.#':
        if row[i] == choice or row[i] == '?':
            if choice == '.' and cur == 0:
                res += get_score(row, nums, i + 1, j, 0)
            elif choice == '.' and cur > 0 and j < len(nums) and nums[j] == cur:
                res += get_score(row, nums, i + 1, j + 1, 0)
            elif choice == '#':
                res += get_score(row, nums, i + 1, j, cur + 1)
    dp[key] = res
    return res


def part2():
    with open(fname) as f:
        all_lines = f.read()
    lines = all_lines.strip().split('\n')
    res = 0
    for line in lines:
        row, nums = line.split()
        nums = list(map(int, nums.split(',')))
        res += get_score('?'.join([row] * 5), nums * 5, 0, 0, 0)
        dp.clear()
    print(res)
    


if __name__ == "__main__":
    part1()
    part2()
