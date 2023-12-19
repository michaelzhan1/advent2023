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


if __name__ == "__main__":
    part1()
    part2()
