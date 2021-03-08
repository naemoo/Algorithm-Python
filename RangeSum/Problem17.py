# https://www.acmicpc.net/problem/19584
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
points = [tuple(map(int, read().strip().split())) for _ in range(n)]
arr = defaultdict(int)
for _ in range(m):
    st, to, w = map(int, read().strip().split())
    st, to = points[st - 1][1], points[to - 1][1]
    st, to = min(st, to), max(st, to)
    arr[st] += w
    arr[to + 1] -= w
    print(st, to)
ans = -float('inf')
tmp = 0
for e in sorted(arr.items()):
    tmp += e[1]
    ans = max(ans, tmp)
print(ans)
print(sorted(arr.items()))
