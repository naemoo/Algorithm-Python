# https://www.acmicpc.net/problem/16681
import sys
from collections import defaultdict
from heapq import heappop, heappush

read = sys.stdin.readline
n, m, d, e = map(int, read().strip().split())
adj = defaultdict(list)
mountains = list(map(int, read().strip().split()))

for _ in range(m):
    a, b, c = map(int, read().strip().split())
    a, b = a - 1, b - 1
    if mountains[a] < mountains[b]:
        adj[a + 1].append((b + 1, c))
    elif mountains[a] > mountains[b]:
        adj[b + 1].append((a + 1, c))


def dijkstra(ascend=True):
    start = 1 if ascend else n
    q = [(0, start)]
    visit = [float('inf') for _ in range(n + 1)]
    visit[start] = 0

    while q:
        cost, cur = heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in adj[cur]:
            nxt_cost = cost + nw
            if nxt_cost < visit[nxt]:
                heappush(q, (nxt_cost, nxt))
                visit[nxt] = nxt_cost
    return visit


a = dijkstra()[1:]
b = dijkstra(False)[1:]
c = list(map(sum, zip(a, b)))
ans = -float('inf')
for i in range(n):
    he = mountains[i] * e
    stamina = c[i] * d
    if he == float('inf') or stamina == float('inf'):
        continue
    ans = max(ans, he - stamina)
print(ans if ans != -float('inf') else 'Impossible')
