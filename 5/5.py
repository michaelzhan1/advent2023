def part1():
    maps = []
    with open('test.in') as f:
        lines = f.read().strip().split('\n\n')
        seeds = list(map(int, lines[0].split(':')[1].strip().split()))
        for line in lines[1:]:
            maps.append([])
            data = line.split(':')[1]
            for mapping in data.strip().split('\n'):
                end, start, count = list(map(int, mapping.split()))
                maps[-1].append((start, start + count - 1, end - start))
    
    res = []
    for seed in seeds:
        current = seed
        for mapping in maps:
            for start, end, diff in mapping:
                if start <= current <= end:
                    current += diff
                    break
        res.append(current)
    print(min(res))


def part2():
    def check_intersect(a, b, c, d):
        return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d

    maps = []
    with open('5.in') as f:
        lines = f.read().strip().split('\n\n')
        seed_input = list(map(int, lines[0].split(':')[1].strip().split()))
        seed_ranges = []
        for i in range(0, len(seed_input), 2):
            seed_ranges.append((seed_input[i], seed_input[i] + seed_input[i + 1] - 1))
        for line in lines[1:]:
            maps.append([])
            data = line.split(':')[1]
            for mapping in data.strip().split('\n'):
                end, start, count = list(map(int, mapping.split()))
                maps[-1].append((start, start + count - 1, end - start))
    
    for mapping in maps:
        new_ranges = []
        for start, end, diff in mapping:
            remaining_ranges = []
            for seed_start, seed_end in seed_ranges:
                if check_intersect(start, end, seed_start, seed_end):
                    new_start = max(start, seed_start)
                    new_end = min(end, seed_end)
                    new_ranges.append((new_start + diff, new_end + diff))
                    if seed_start < start:
                        remaining_ranges.append((seed_start, new_start - 1))
                    if seed_end > end:
                        remaining_ranges.append((new_end + 1, seed_end))
                else:
                    remaining_ranges.append((seed_start, seed_end))
            seed_ranges = remaining_ranges
        seed_ranges = new_ranges + remaining_ranges
    print(min(seed_ranges)[0])


if __name__ == "__main__":
    part1()
    part2()
