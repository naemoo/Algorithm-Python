# https://www.acmicpc.net/problem/11779
import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
m = int(read().strip())
bus = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(m):
    st, to, w = map(int, read().strip().split())
    bus[st][to] = min(bus[st][to], w)

start, end = map(int, read().strip().split())


def dijkstra(start, end):
    visit = [float('inf') for _ in range(n + 1)]
    visit[start] = 0
    path = [-1 for _ in range(n + 1)]
    q = []
    q.append((0, start))

    while q:
        cost, cur = heapq.heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in bus[cur].items():
            nextCost = nw + cost
            if nextCost < visit[nxt]:
                visit[nxt] = nextCost
                path[nxt] = cur
                heapq.heappush(q, (nextCost, nxt))
    print(visit[end])
    idx = end
    ans = []
    while idx != -1:
        ans.append(idx)
        idx = path[idx]
    ans.reverse()
    print(len(ans))
    for e in ans:
        print(e, end=' ')


dijkstra(start, end)
