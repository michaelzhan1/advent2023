fname = '15.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    line = all_lines.strip()
    res = 0
    for s in line.split(','):
        cur = 0
        for c in s:
            cur += ord(c)
            cur *= 17
            cur %= 256
        res += cur
    print(res)
    

def part2():
    with open(fname) as f:
        all_lines = f.read()
    line = all_lines.strip()
    res = 0

    def hash(s):
        cur = 0
        for c in s:
            cur += ord(c)
            cur *= 17
            cur %= 256
        return cur
    
    boxes = [[] for _ in range(256)]

    for s in line.split(','):
        if '=' in s:
            label = s.split('=')[0].strip()
            val = s[s.index('=') + 1]
            cur = hash(label)
            if label in [boxes[cur][i][0] for i in range(len(boxes[cur]))]:
                for i in range(len(boxes[cur])):
                    if boxes[cur][i][0] == label:
                        boxes[cur][i] = (label, val)
                        break
            else:
                boxes[cur].append((label, val))
        elif '-' in s:
            label = s.split('-')[0].strip()
            cur = hash(label)
            for i in range(len(boxes[cur])):
                if boxes[cur][i][0] == label:
                    boxes[cur].pop(i)
                    break
    res = 0
    for i in range(256):
        for j in range(len(boxes[i])):
            res += (i + 1) * (j + 1) * int(boxes[i][j][1])
    print(res)


if __name__ == '__main__':
    part1()
    part2()
