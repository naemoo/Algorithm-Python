# https://www.acmicpc.net/problem/2096
import sys
from copy import deepcopy

read = sys.stdin.readline
n = int(read().strip())
maxDp = list(map(int, read().strip().split()))
minDp = deepcopy(maxDp)

for _ in range(n - 1):
    a, b, c = map(int, read().strip().split())
    maxDp = [max(maxDp[:2]) + a
        , max(maxDp) + b
        , max(maxDp[1:]) + c]
    minDp = [min(minDp[:2]) + a
        , min(minDp) + b
        , min(minDp[1:]) + c]

print(max(maxDp), min(minDp))
