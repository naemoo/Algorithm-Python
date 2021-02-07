# https://www.acmicpc.net/problem/5719
import heapq
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())


def dijkstra():
    visit = [float('inf') for _ in range(n)]
    visit[start] = 0
    q = [(0, start)]
    while q:
        cost, cur = heapq.heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in adj[cur].items():
            nw_cost = nw + cost
            if visit[nxt] > nw_cost:
                heapq.heappush(q, (nw_cost, nxt))
                visit[nxt] = nw_cost
    return visit


while n and m:
    start, end = map(int, read().strip().split())
    adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
    adj_r = defaultdict(list)
    while m:
        a, b, w = map(int, read().strip().split())
        adj[a][b] = w
        adj_r[b].append(a)
        m -= 1

    logs = [[] for _ in range(n)]
    visit = dijkstra()
    q = deque()
    q.append(end)
    while q:
        cur = q.popleft()
        if cur == start:
            continue
        for nxt in adj_r[cur]:
            if visit[nxt] + adj[nxt][cur] == visit[cur]:
                del adj[nxt][cur]
                q.append(nxt)

    visit = dijkstra()
    print(visit[end] if visit[end] != float('inf') else -1)
    adj.clear()
    n, m = map(int, read().strip().split())
