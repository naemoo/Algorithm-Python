# https://www.acmicpc.net/problem/1450
import sys
from itertools import combinations

read = sys.stdin.readline
n, c = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))

a = arr[:n // 2]
b = arr[n // 2:]
sA = []
sB = []

for i in range(len(a) + 1):
    for e in combinations(a, i):
        sA.append(sum(e))

for i in range(len(b) + 1):
    for e in combinations(b, i):
        sB.append(sum(e))


def getIdx(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return r

sB.sort()
ret = 0
for e in sA:
    u = getIdx(sB, c - e)
    ret += u
print(ret)
