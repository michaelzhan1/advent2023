from functools import cache
from math import lcm
import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def part1():
    res = 0
    with open('8.in') as f:
        lines = f.read().strip()

    lines = lines.split('\n')
    directions = list(lines[0].strip())
    info = lines[2:]
    nodes = {}
    for s in info:
        s = s.split()
        start = s[0]
        left_val = s[2][1:-1]
        right_val = s[3][:-1]
        if start not in nodes:
            nodes[start] = Node(start)
        if left_val not in nodes:
            nodes[left_val] = Node(left_val)
        if right_val not in nodes:
            nodes[right_val] = Node(right_val)
        nodes[start].left = nodes[left_val]
        nodes[start].right = nodes[right_val]
    res = 0
    cur = 'AAA'
    while cur != 'ZZZ':
        d = directions[res % len(directions)]
        if d == 'L':
            cur = nodes[cur].left.val
        else:
            cur = nodes[cur].right.val
        res += 1
    print(res)


def part2():
    graph = {}
    with open('8.in') as f:
        lines = f.read().strip()

    lines = lines.split('\n')
    directions = list(lines[0])
    info = lines[2:]
    for s in info:
        start, left, right = re.findall(r'\w+', s)
        graph[start] = (left, right)
    cur = [n for n in graph if n[2] == 'A']
    cycle_length = []
    for n in cur:
        res = 0
        while n[2] != 'Z':
            n = graph[n][directions[res % len(directions)] == 'R']
            res += 1
        cycle_length.append(res)
    print(lcm(*cycle_length))


if __name__ == "__main__":
    part1()
    part2()
