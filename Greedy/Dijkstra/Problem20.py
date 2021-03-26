# https://www.acmicpc.net/problem/17835
import sys
from collections import defaultdict
from heapq import heappop, heappush

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
adj = defaultdict(list)

while m:
    a, b, w = map(int, read().strip().split())
    adj[b].append((a, w))
    m -= 1

visit = [float('inf')] * (n + 1)
company = list(map(int, read().strip().split()))
q = []
for e in company:
    visit[e] = 0
    q.append((0, e))

while q:
    cost, cur = heappop(q)

    if visit[cur] < cost:
        continue

    for nxt, nw in adj[cur]:
        nxt_cost = nw + cost
        if nxt_cost < visit[nxt]:
            heappush(q, (nxt_cost, nxt))
            visit[nxt] = nxt_cost
ans = [0, 0]
for i, e in enumerate(visit[1:], start=1):
    if ans[1] < e:
        ans[0] = i
        ans[1] = e

print(*ans, sep='\n')
