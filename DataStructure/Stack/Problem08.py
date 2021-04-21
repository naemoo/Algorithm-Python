# https://www.acmicpc.net/problem/17298
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = list(map(int, read().strip().split()))
s = []
ans = [-1 for _ in range(n)]

for i, e in enumerate(arr):
    while s and s[-1][1] < e:
        a, b = s.pop()
        ans[a] = e
    s.append((i, e))

for e in ans:
    print(e, end=' ')
