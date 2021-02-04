# https://www.acmicpc.net/problem/1854
import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))

while m:
    a, b, c = map(int, read().strip().split())
    adj[a][b] = min(c, adj[a][b])
    m -= 1

visit = [[] for _ in range(n + 1)]
q = [(0, 1)]
visit[1].append(0)

while q:
    cost, cur = heapq.heappop(q)

    for nxt, nw in adj[cur].items():
        nextCost = cost + nw

        if len(visit[nxt]) < k:
            heapq.heappush(visit[nxt], -nextCost)
            heapq.heappush(q, (nextCost, nxt))
        elif -visit[nxt][0] > nextCost:
            heapq.heappop(visit[nxt])
            heapq.heappush(visit[nxt], -nextCost)
            heapq.heappush(q, (nextCost, nxt))

for i in range(1, n + 1):
    if len(visit[i]) < k:
        print(-1)
    else:
        print(-visit[i][0])
