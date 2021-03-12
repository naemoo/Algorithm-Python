# https://www.acmicpc.net/problem/1374
import sys

read = sys.stdin.readline
n = int(read().strip())
q = []
for _ in range(n):
    cn, st, end = map(int, read().strip().split())
    q.append((st, 1))
    q.append((end, -1))
q.sort()
tmp = 0
ans = 0
for a, b in q:
    tmp += b
    ans = max(tmp, ans)
print(ans)
