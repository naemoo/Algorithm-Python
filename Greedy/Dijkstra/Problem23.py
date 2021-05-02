# https://www.acmicpc.net/problem/16118
import sys
from collections import defaultdict
from heapq import heappush, heappop

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(m):
    a, b, c = map(int, read().strip().split())
    adj[a][b] = min(c * 2, adj[a][b])
    adj[b][a] = min(c * 2, adj[b][a])


def get_fox_Distance():
    q = [(0, 1)]
    visit = [float('inf')] * (n + 1)
    visit[1] = 0

    while q:
        cost, cur = heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, w in adj[cur].items():
            nw = w + cost
            if nw < visit[nxt]:
                heappush(q, (nw, nxt))
                visit[nxt] = nw

    return visit


def get_wolf_distance():
    q = [(0, 1, 1)]
    visit = [[float('inf') for _ in range(2)] for _ in range(n + 1)]
    visit[1][1] = 0

    while q:
        cost, cur, isFast = heappop(q)

        if visit[cur][isFast] < cost:
            continue

        for nxt, w in adj[cur].items():
            nw = cost + (w // 2 if isFast else 2 * w)
            nxt_state = 1 - isFast

            if nw < visit[nxt][nxt_state]:
                heappush(q, (nw, nxt, nxt_state))
                visit[nxt][nxt_state] = nw

    return visit


visit_fox = get_fox_Distance()
visit_wolf = get_wolf_distance()

ans = 0
for fox, wolf in zip(visit_fox, visit_wolf):
    if fox < min(wolf):
        ans += 1

print(ans)
