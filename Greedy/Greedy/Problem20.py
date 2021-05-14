# https://www.acmicpc.net/problem/13907
import sys
from collections import defaultdict
from heapq import heappop, heappush

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
start, end = map(int, read().strip().split())
adj = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, read().strip().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

visit = [[float('inf') for _ in range(n)] for _ in range(n + 1)]

q = [(0, start, 0)]
visit[start][0] = 0

while q:
    cost, cur, cnt = heappop(q)
    flag = False

    for i in range(cnt):
        if visit[cur][i] < cost:
            flag = True
            break

    if end == cur:
        continue

    if flag or visit[cur][cnt] < cost:
        continue

    for nxt, nw in adj[cur]:
        nxt_cost = cost + nw

        if cnt + 1 < n and nxt_cost < visit[nxt][cnt + 1]:
            visit[nxt][cnt + 1] = nxt_cost
            heappush(q, (nxt_cost, nxt, cnt + 1))

total = 0
p = [0]
for _ in range(k):
    p.append(int(read().strip()))

for e in p:
    total += e
    ans = float('inf')
    for i in range(n):
        tmp = visit[end][i] + i * total
        ans = min(ans, tmp)
    print(ans)
