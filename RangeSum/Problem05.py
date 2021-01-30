# https://www.acmicpc.net/problem/1275
import sys

inp = sys.stdin.readline
n, q = map(int, inp().strip().split())
arr = [e for e in map(int, inp().strip().split())]
tree = [0] * (n + 1)


def add(idx, num):
    idx += 1
    while idx < len(tree):
        tree[idx] += num
        idx += (idx & -idx)


def sum(idx):
    idx += 1
    ret = 0
    while idx > 0:
        ret += tree[idx]
        idx &= idx - 1
    return ret


def rangeSum(st, to):
    return sum(to) - sum(st - 1)


for i, e in enumerate(arr):
    add(i, e)

for _ in range(q):
    x, y, a, b = map(int, inp().strip().split())
    print(rangeSum(min(x - 1, y - 1), max(x - 1, y - 1)))
    add(a - 1, b - arr[a - 1])
    arr[a - 1] = b

