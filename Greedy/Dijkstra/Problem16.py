# https://www.acmicpc.net/problem/1884
import sys
from collections import defaultdict
from heapq import heappush, heappop

read = sys.stdin.readline
k = int(read().strip())
n = int(read().strip())
r = int(read().strip())
adj = defaultdict(list)

while r:
    s, d, l, t = map(int, read().strip().split())
    adj[s].append((d, l, t))
    r -= 1

q = []
heappush(q, (0, 0, 1))
max_cost = k + 1
visit = [[float('inf') for _ in range(max_cost)] for _ in range(n + 1)]

while q:
    distance, cost, cur = heappop(q)

    if visit[cur][cost] < distance:
        continue

    for nxt, nw, n_cost in adj[cur]:
        nxt_distance = nw + distance
        nxt_cost = n_cost + cost
        if nxt_cost > k:
            continue
        if visit[nxt][nxt_cost] > nxt_distance:
            heappush(q, (nxt_distance, nxt_cost, nxt))
            visit[nxt][nxt_cost] = nxt_distance

ans = min(visit[n])
print(ans if ans != float('inf') else -1)
