from copy import deepcopy


fname = '19.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()
    rules, lines = all_lines.split('\n\n')
    rules = rules.split('\n')
    lines = lines.split('\n')

    xmas = []
    for line in lines:
        line = line.strip('{').strip('}').split(',')
        xmas.append({})
        xmas[-1]['x'] = int(line[0].split('=')[1])
        xmas[-1]['m'] = int(line[1].split('=')[1])
        xmas[-1]['a'] = int(line[2].split('=')[1])
        xmas[-1]['s'] = int(line[3].split('=')[1])
    
    logic = {}
    for rule in rules:
        rule = rule.strip('}').split('{')
        name = rule[0]
        rule = rule[1].split(',')
        logic[name] = []
        for r in rule:
            if ':' not in r:
                logic[name].append(r)
                continue
            target = r.split(':')[1]
            letter = r[0]
            compare = r[1]
            value = int(r[2:].split(':')[0])
            logic[name].append((letter, compare, value, target))
    
    res = 0
    for line in xmas:
        work = 'in'
        while True:
            if work == 'A':
                res += sum(line.values())
                break
            elif work == 'R':
                break

            for i in range(len(logic[work])):
                if i == len(logic[work]) - 1:
                    work = logic[work][i]
                else:
                    letter, compare, value, target = logic[work][i]
                    if compare == '>':
                        if line[letter] > value:
                            work = target
                            break
                    elif compare == '<':
                        if line[letter] < value:
                            work = target
                            break

    print(res)


def part2():
    with open(fname) as f:
        all_lines = f.read()
    rules, _ = all_lines.split('\n\n')
    rules = rules.split('\n')
    logic = {}
    for rule in rules:
        rule = rule.strip('}').split('{')
        name = rule[0]
        rule = rule[1].split(',')
        logic[name] = []
        for r in rule:
            if ':' not in r:
                logic[name].append(r)
                continue
            target = r.split(':')[1]
            letter = r[0]
            compare = r[1]
            value = int(r[2:].split(':')[0])
            logic[name].append((letter, compare, value, target))


    def evaluate(ranges):
        res = 1
        res *= ranges['x'][1] - ranges['x'][0] + 1
        res *= ranges['m'][1] - ranges['m'][0] + 1
        res *= ranges['a'][1] - ranges['a'][0] + 1
        res *= ranges['s'][1] - ranges['s'][0] + 1
        return res

    res = 0
    stack = []
    initial_ranges = {
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000],
    }
    stack.append(('in', initial_ranges))
    while stack:
        work, ranges = stack.pop()
        bad = False
        for letter in ranges:
            if ranges[letter][1] < ranges[letter][0]:
                bad = True
                break
        if bad:
            continue

        if work == 'A':
            res += evaluate(ranges)
            continue
        elif work == 'R':
            continue
        else:
            for i in range(len(logic[work])):
                if i == len(logic[work]) - 1:
                    stack.append((logic[work][i], ranges))
                    break

                letter, compare, value, target = logic[work][i]
                if compare == '>':
                    if ranges[letter][0] > value:
                        stack.append((target, ranges))
                        break
                    elif ranges[letter][1] < value:
                        continue
                    else:
                        new_ranges = deepcopy(ranges)
                        new_ranges[letter][0] = value + 1
                        stack.append((target, new_ranges))
                        ranges[letter][1] = value
                        continue
                elif compare == '<':
                    if ranges[letter][1] < value:
                        stack.append((target, ranges))
                        break
                    elif ranges[letter][0] > value:
                        continue
                    else:
                        new_ranges = deepcopy(ranges)
                        new_ranges[letter][1] = value - 1
                        stack.append((target, new_ranges))
                        ranges[letter][0] = value
                        continue
    print(res)

if __name__ == "__main__":
    part1()
    part2()
