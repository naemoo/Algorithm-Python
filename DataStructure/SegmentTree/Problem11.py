# https://www.acmicpc.net/problem/1517
import sys
from bisect import bisect_left

read = sys.stdin.readline
n = int(read().strip())
arr = list(map(int, read().strip().split()))
tree = [0 for _ in range(n + 1)]


def update(idx, val=1):
    idx += 1
    while idx > 0:
        tree[idx] += val
        idx -= (idx & -idx)


def getSum(idx):
    ret = 0
    idx += 1
    while idx < len(tree):
        ret += tree[idx]
        idx += (idx & -idx)
    return ret


sorted_arr = sorted(set(arr))
ans = 0
for e in arr:
    idx = bisect_left(sorted_arr, e)
    ans += getSum(idx + 1)
    update(idx)

print(ans)
