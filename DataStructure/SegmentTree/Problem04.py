# https://www.acmicpc.net/problem/2243
import sys

read = sys.stdin.readline
n = int(read().strip())

tree = [0] * 10000001


def update(idx, e):
    while idx < len(tree):
        tree[idx] += e
        idx += (idx & -idx)


def sum(idx):
    ret = 0
    while idx > 0:
        ret += tree[idx]
        idx -= (idx & -idx)
    return ret


for _ in range(n):
    tmp = tuple(map(int, read().strip().split()))
    if len(tmp) == 3:
        a, b, c = tmp
    else:
        a, b = tmp

    if a == 1:
        l, r = 0, 10000001
        while l < r:
            mid = (l + r) // 2
            if sum(mid) < b:
                l = mid + 1
            else:
                r = mid
        print(r)
        update(r, -1)

    elif a == 2:
        update(b, c)
