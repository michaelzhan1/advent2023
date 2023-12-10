def main():
    res = 0
    nums = {}
    matrix = []
    with open('3.in') as f:
        for line in f.readlines():
            line = line.strip()
            matrix.append([])
            for i in range(len(line)):
                matrix[-1].append(line[i])
    
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        j = 0
        line = matrix[i]
        while j < len(line):
            if line[j] in set('0123456789'):
                k = j
                while k < len(line) and line[k] in set('0123456789'):
                    k += 1
                num = int(''.join(line[j:k]))
                for x in range(j, k):
                    nums[(i, x)] = num
                j = k
            else:
                j += 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] not in set('0123456789.'):
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(m, j + 2)):
                        if (x, y) in nums:
                            res += nums[(x, y)]
                            nums[(x, y)] = 0
                            idx = 0
                            while idx < m and (x, y + idx) in nums:
                                nums[(x, y + idx)] = 0
                                idx += 1
                            idx = 0
                            while idx < m and (x, y - idx) in nums:
                                nums[(x, y - idx)] = 0
                                idx += 1
    print(res)

    used = set()
    matrix = []
    nums = {}
    with open('3.in') as f:
        for line in f.readlines():
            line = line.strip()
            matrix.append([])
            for i in range(len(line)):
                matrix[-1].append(line[i])
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        j = 0
        line = matrix[i]
        while j < len(line):
            if line[j] in set('0123456789'):
                k = j
                while k < len(line) and line[k] in set('0123456789'):
                    k += 1
                num = int(''.join(line[j:k]))
                for x in range(j, k):
                    nums[(i, x)] = num
                j = k
            else:
                j += 1
    
    res2 = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '*':
                gear_ratio = 1
                count = 0
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(m, j + 2)):
                        if (x, y) in nums and (x, y) not in used:
                            gear_ratio *= nums[(x, y)]
                            count += 1
                            nums[(x, y)] = 0
                            used.add((x, y))
                            idx = 1
                            while idx < m and (x, y + idx) in nums:
                                used.add((x, y + idx))
                                nums[(x, y + idx)] = 0
                                idx += 1
                            idx = 1
                            while idx < m and (x, y - idx) in nums:
                                used.add((x, y - idx))
                                nums[(x, y - idx)] = 0
                                idx += 1
                if count == 2:
                    res2 += gear_ratio
    print(res2)


if __name__ == "__main__":
    main()