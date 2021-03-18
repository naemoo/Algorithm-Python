# https://www.acmicpc.net/problem/14554
import sys
from collections import defaultdict
from heapq import heappush, heappop

read = sys.stdin.readline
n, m, s, e = map(int, read().strip().split())
adj = defaultdict(list)

while m:
    a, b, c = map(int, read().strip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
    m -= 1

visit = [float('inf') for _ in range(n + 1)]
counts = [0 for _ in range(n + 1)]
visit[s] = 0
counts[s] = 1
q = [(0, s)]

while q:
    cost, cur = heappop(q)

    if visit[cur] < cost:
        continue

    for nxt, nw in adj[cur]:
        nxt_cost = cost + nw
        if nxt_cost < visit[nxt]:
            heappush(q, (nxt_cost, nxt))
            counts[nxt] = counts[cur]
            visit[nxt] = nxt_cost
        elif nxt_cost == visit[nxt]:
            counts[nxt] = (counts[cur] + counts[nxt]) % 1000000009

print(counts[e])
