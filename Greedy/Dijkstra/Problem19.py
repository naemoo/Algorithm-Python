# https://www.acmicpc.net/problem/2325
import sys
from collections import defaultdict
from copy import deepcopy
from heapq import heappop, heappush

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(list)

while m:
    a, b, w = map(int, read().strip().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
    m -= 1

lions = [-1 for _ in range(n + 1)]


def dijkstra(u=0, v=0):
    q = [(0, 1)]
    visit = [float('inf') for _ in range(n + 1)]
    visit[1] = 0
    del_edge = ((u, v), (v, u))
    while q:
        cost, cur = heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in adj[cur]:
            nxt_cost = nw + cost

            if del_edge[0] == (cur, nxt) or del_edge[1] == (cur, nxt):
                continue

            if nxt_cost < visit[nxt]:
                heappush(q, (nxt_cost, nxt))
                visit[nxt] = nxt_cost
                lions[nxt] = cur

    return visit[n]


dijkstra()
parent = deepcopy(lions)
ans = 0
u = n
while lions[u] != -1:
    tmp = dijkstra(parent[u], u)
    u = parent[u]
    if tmp != float('inf'):
        ans = max(tmp, ans)
print(ans)
