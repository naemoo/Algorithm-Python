# https://www.acmicpc.net/problem/13904
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n = int(read().strip())
assignments = [tuple(map(int, read().strip().split())) for _ in range(n)]
assignments.sort()
q = []

for d, w, in assignments:
    if d > len(q):
        heappush(q, w)
    else:
        if q and q[0] < w:
            heappop(q)
            heappush(q, w)
print(sum(q))