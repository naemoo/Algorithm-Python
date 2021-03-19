# https://www.acmicpc.net/problem/12738
import sys
from bisect import bisect_left

read = sys.stdin.readline
n = int(read().strip())
lis = []
arr = list(map(int, read().strip().split()))
for i, e in enumerate(arr):
    idx = bisect_left(lis, e)
    if idx == len(lis):
        lis.append(e)
    else:
        lis[idx] = e

print(len(lis))
