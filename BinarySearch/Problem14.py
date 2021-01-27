# https://www.acmicpc.net/problem/2805
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
l, r = 0, max(arr)

while l < r:
    mid = (l + r + 1) // 2
    total = 0
    for tree in arr:
        total += tree - mid if tree - mid > 0 else 0
    if total >= m:
        l = mid
    else:
        r = mid - 1
print(l)
