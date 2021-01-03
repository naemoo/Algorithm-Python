# https://www.acmicpc.net/problem/2109
import heapq
import sys

read = sys.stdin.readline
n = int(read().strip())

lectures = []

maxDay = 0

for _ in range(n):
    p, d = map(int, read().strip().split())
    lectures.append((d, p))
    maxDay = max(maxDay, d)
lectures = sorted(lectures, reverse=True)
q = []

idx = 0
ans = 0
for day in range(maxDay, 0, -1):

    while idx < len(lectures) and day <= lectures[idx][0]:
        heapq.heappush(q, -lectures[idx][1])
        idx += 1

    if q:
        ans += (-heapq.heappop(q))
print(ans)