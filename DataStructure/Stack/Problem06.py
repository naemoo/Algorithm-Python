# https://www.acmicpc.net/problem/6198
import sys

read = sys.stdin.readline
n = int(read().strip())
buildings = [int(read().strip()) for _ in range(n)]
s = []
ans = 0
for i, building in enumerate(buildings):
    while s and s[-1][1] <= building:
        idx, h = s.pop()
        ans += i - idx - 1
    s.append((i, building))

while s:
    i, h = s.pop()
    ans += n - 1 - i
print(ans)
