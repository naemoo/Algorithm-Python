# https://www.acmicpc.net/problem/1202
import heapq
import sys

inp = sys.stdin.readline
n, k = map(int, inp().strip().split())
jewelries = []
for _ in range(n):
    m, v = map(int, inp().strip().split())
    jewelries.append((m, v))
bags = []

for _ in range(k):
    bags.append(int(inp().strip()))

bags.sort()
jewelries.sort()
ans = 0

pq = []
idx = 0
for b in bags:
    while idx < len(jewelries) and jewelries[idx][0] <= b:
        m, v = jewelries[idx][0], jewelries[idx][1]
        heapq.heappush(pq, (-v, m))
        idx += 1
    if pq:
        ans += (-heapq.heappop(pq)[0])
print(ans)
