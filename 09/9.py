def predict(pattern):
    if pattern[0] == pattern[-1]:
        return pattern[-1]
    else:
        return pattern[-1] + predict([pattern[i] - pattern[i-1] for i in range(1, len(pattern))])

def part1():
    patterns = []
    with open('9.in') as f:
        for line in f.readlines():
            patterns.append(list(map(int, line.strip().split())))
    print(sum([predict(pattern) for pattern in patterns]))

def predict_before(pattern):
    if pattern[0] == pattern[-1] == 0:
        return pattern[-1]
    else:
        return pattern[0] - predict_before([pattern[i] - pattern[i-1] for i in range(1, len(pattern))])

def part2():
    patterns = []
    with open('9.in') as f:
        for line in f.readlines():
            patterns.append(list(map(int, line.strip().split())))
    print(sum([predict_before(pattern) for pattern in patterns]))


if __name__ == "__main__":
    part1()
    part2()