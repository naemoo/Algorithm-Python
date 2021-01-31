# https://www.acmicpc.net/problem/3653
import sys
from collections import defaultdict

read = sys.stdin.readline
t = int(read().strip())


def update(idx, e):
    while idx > 0:
        tree[idx] += e
        idx -= (idx & -idx)


def getSum(idx):
    ret = 0
    while idx < len(tree):
        ret += tree[idx]
        idx += (idx & -idx)
    return ret


while t:
    n, m = map(int, read().strip().split())
    tree = [0 for _ in range(n + m + 1)]
    t_idx = 1
    index = defaultdict(int)
    for i in range(1, n + 1):
        update(i, 1)
        index[i] = n - t_idx + 1
        t_idx += 1
    for e in map(int, read().strip().split()):
        tmp = index[e]
        update(tmp, -1)
        print(getSum(tmp), end=' ')
        index[e] = t_idx
        update(t_idx, 1)
        t_idx += 1
    print()
    index.clear()
    t -= 1
