# https://www.acmicpc.net/problem/1184
import sys
from collections import Counter

read = sys.stdin.readline
n = int(read().strip())
farms = [list(map(int, read().strip().split())) for _ in range(n)]
ps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + farms[i - 1][j - 1]

totals = []


def get_sum(i, j, x, y):
    if i + x > n or j + y > n:
        return float('inf')
    a, b, c, d = i, j, i + x, j + y
    return ps[c][d] - ps[c][b] - ps[a][d] + ps[a][b]


def left_up(i, j):
    ret = []
    for x in range(1, i + 2):
        for y in range(1, j + 2):
            tmp = get_sum(i - x + 1, j - y + 1, x, y)
            if tmp != float('inf'):
                ret.append(tmp)
    return ret


def right_down(i, j):
    ret = []
    for x in range(1, n - i + 1):
        for y in range(1, n - j + 1):
            tmp = get_sum(i, j, x, y)
            if tmp != float('inf'):
                ret.append(tmp)
    return ret


def left_down(i, j):
    ret = []
    for x in range(1, n - i + 1):
        for y in range(1, j + 2):
            tmp = get_sum(i, j - y + 1, x, y)
            if tmp != float('inf'):
                ret.append(tmp)
    return ret


def right_up(i, j):
    ret = []
    for x in range(1, i + 2):
        for y in range(1, n - j + 1):
            tmp = get_sum(i - x + 1, j, x, y)
            if tmp != float('inf'):
                ret.append(tmp)
    return ret

ans = 0
for i in range(n):
    for j in range(n):
        lu = Counter(left_up(i, j))
        rd = right_down(i + 1, j + 1)
        for e in rd:
            if e in lu.keys():
                ans += lu[e]
        ru = Counter(right_up(i, j + 1))
        ld = left_down(i + 1, j)
        for e in ld:
            if e in ru.keys():
                ans += ru[e]
print(ans)
