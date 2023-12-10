def part1():
    res = 1
    with open('6.in') as f:
        all_lines = f.read()
    time_line, distance_line = all_lines.strip().split('\n')
    times = [int(x) for x in time_line.split(':')[1].strip().split()]
    distances = [int(x) for x in distance_line.split(':')[1].strip().split()]
    for i in range(len(times)):
        race_wins = 0
        time = times[i]
        dist_to_beat = distances[i]
        for i in range(time + 1):
            speed = i
            if speed * (time - speed) > dist_to_beat:
                race_wins += 1
        res *= race_wins
    print(res)


def part2():
    res = 0
    with open('6.in') as f:
        all_lines = f.read()
    time_line, distance_line = all_lines.strip().split('\n')
    time = int(''.join(time_line.split(':')[1].strip().split()))
    distance = int(''.join(distance_line.split(':')[1].strip().split()))
    # binary search to find smallest time that works
    def check(t):
        if t * (time - t) > distance:
            return True
        return False
    right = (time + 1) // 2
    left = 0
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    start = left
    end = time - left
    print(end - start + 1)


if __name__ == '__main__':
    part1()
    part2()