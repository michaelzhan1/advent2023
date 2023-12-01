def find_number(s):
    res = ''
    for i in range(len(s)):
        if s[i].isdigit():
            res += s[i]
            break
    
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            res += s[i]
            break
    
    return int(res) if res else 0

def find_number2(s):
    res = ''
    num_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    for i in range(len(s)):
        if s[i].isdigit():
            res += s[i]
            break
        found = False
        for n in num_map:
            if s[i:].startswith(n):
                res += str(num_map[n])
                found = True
                break
        if found:
            break
    
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            res += s[i]
            break
        found = False
        for n in num_map:
            if s[:i + 1].endswith(n):
                res += str(num_map[n])
                found = True
                break
        if found:
            break
    return int(res)



def main():
    res = 0
    with open('1.in') as f:
        for line in f.readlines():
            res += find_number(line)
    print(res)

    res = 0
    with open('1.in') as f:
        for line in f.readlines():
            res += find_number2(line)
    print(res) 


if __name__ == "__main__":
    main()