# https://www.acmicpc.net/problem/2517
import sys
from copy import deepcopy

read = sys.stdin.readline
n = int(read())
arr = [-1]
for _ in range(n):
    arr.append(int(read().strip()))

runners = deepcopy(arr)
arr.sort()

def lower(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


for i, e in enumerate(runners):
    runners[i] = lower(arr, e)
maxRunner = max(runne,rs)
tree = [0] * (maxRunner + 1)


def getSum(idx):
    ret = 0
    while idx <= maxRunner:
        ret += tree[idx]
        idx += (idx & -idx)
    return ret


def update(idx, e):
    while idx > 0:
        tree[idx] += e
        idx -= (idx & -idx)


for i, runner in enumerate(runners):
    if i == 0:
        continue
    update(runner, 1)
    print(getSum(runner))
