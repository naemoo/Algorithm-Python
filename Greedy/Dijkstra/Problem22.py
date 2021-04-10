# https://www.acmicpc.net/problem/11952
import sys
from collections import defaultdict
from heapq import heappush, heappop

read = sys.stdin.readline
n, m, k, s = map(int, read().strip().split())
p, q = map(int, read().strip().split())
adj = defaultdict(list)
queue = []
safe_distance = [float('inf') for _ in range(n + 1)]
z_cities = set()

for _ in range(k):
    z_city = int(read().strip())
    queue.append((0, z_city))
    safe_distance[z_city] = 0
    z_cities.add(z_city)

for _ in range(m):
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    adj[b].append(a)

while queue:
    cost, cur = heappop(queue)

    if safe_distance[cur] < cost:
        continue

    for nxt in adj[cur]:
        nxt_cost = cost + 1
        if nxt_cost < safe_distance[nxt]:
            heappush(queue, (nxt_cost, nxt))
            safe_distance[nxt] = nxt_cost

queue.append((0, 1))
visit = [float('inf') for _ in range(n + 1)]

while queue:
    cost, cur = heappop(queue)

    if visit[cur] < cost:
        continue

    for nxt in adj[cur]:
        if nxt == n:
            nxt_cost = cost
        else:
            nxt_cost = cost + (p if safe_distance[nxt] > s else q)

        if nxt in z_cities:
            continue

        if nxt_cost < visit[nxt]:
            visit[nxt] = nxt_cost
            heappush(queue, (nxt_cost, nxt))

print(visit[n])
