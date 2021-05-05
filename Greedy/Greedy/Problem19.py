# https://www.acmicpc.net/problem/1781
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n = int(read().strip())
problems = [tuple(map(int, read().strip().split())) for _ in range(n)]
problems.sort()
q = []

for d, w in problems:
    if len(q) < d:
        heappush(q, w)
    elif q[0] < w:
        heappop(q)
        heappush(q, w)

print(sum(q))
