# https://www.acmicpc.net/problem/10217
import sys
from collections import defaultdict
from heapq import heappush, heappop

read = sys.stdin.readline
t = int(read().strip())
while t:
    n, m, k = map(int, read().strip().split())
    adj = defaultdict(list)

    for _ in range(k):
        a, b, c, d = map(int, read().strip().split())
        adj[a].append((b, c, d))

    q = []
    heappush(q, (0, 0, 1))
    visit = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    visit[1][0] = 0
    flag = True
    while q:
        time, cost, cur = heappop(q)

        if cur == n:
            print(time)
            flag = False
            break

        if visit[cur][cost] < time:
            continue

        for nxt, nc, nd in adj[cur]:
            nxt_cost = nc + cost
            nxt_time = nd + time
            if nxt_cost > m:
                continue
            if nxt_time < visit[nxt][nxt_cost]:
                visit[nxt][nxt_cost] = nxt_time
                heappush(q, (nxt_time, nxt_cost, nxt))
    adj.clear()
    q.clear()
    if flag:
        print('Poor KCM')
    t -= 1
