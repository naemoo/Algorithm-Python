# https://www.acmicpc.net/problem/1916
import heapq, sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
m = int(read().strip())
bus = defaultdict(list)

for _ in range(m):
    st, to, w = map(int, read().strip().split())
    bus[st].append((to, w))

start, destination = map(int, read().strip().split())

q = [(0, start)]
visit = [float('inf')] * (n + 1)

while q:
    cost, cur = heapq.heappop(q)

    if visit[cur] < cost:
        continue

    for nxt, nw in bus[cur]:
        nextCost = nw + cost
        if nextCost < visit[nxt]:
            heapq.heappush(q, (nextCost, nxt))
            visit[nxt] = nextCost

print(visit[destination])