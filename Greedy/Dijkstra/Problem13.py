# https://programmers.co.kr/learn/courses/30/lessons/72413
import heapq
from collections import defaultdict

adj = defaultdict(lambda: defaultdict(lambda: float('inf')))


def dijkstra(start, n):
    visit = [float('inf') for _ in range(n + 1)]
    visit[start] = 0
    q = [(0, start)]

    while q:
        cost, cur = heapq.heappop(q)

        if visit[cur] < cost:
            continue

        for nxt, nw in adj[cur].items():
            nxtCost = nw + cost
            if visit[nxt] > nxtCost:
                visit[nxt] = nxtCost
                heapq.heappush(q, (nxtCost, nxt))
    return visit


def solution(n, s, a, b, fares):
    ret = float('inf')
    for c, d, f in fares:
        adj[c][d] = min(adj[c][d], f)
        adj[d][c] = min(adj[d][c], f)

    st_to = dijkstra(s, n)
    for v in range(1, n + 1):
        cost = st_to[v]
        v_to = dijkstra(v, n)
        cost += (v_to[a] + v_to[b])
        ret = min(cost, ret)
    ret = min(ret , st_to[a]+ st_to[b])
    print(ret)
    return ret


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
