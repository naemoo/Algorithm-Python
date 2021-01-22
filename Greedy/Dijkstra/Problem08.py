# https://www.acmicpc.net/problem/13308
import heapq
import sys
from collections import deque, defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
gas = deque([int(e) for e in read().strip().split()])
gas.appendleft(0)
path = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(m):
    st, to, w = map(int, read().strip().split())
    path[st][to] = w
    path[to][st] = w


def dijkstra(start):
    maxCost = max(gas)
    visit = [[float('inf') for _ in range(maxCost + 1)] for _ in range(n + 1)]
    q = []
    q.append((0, start, gas[start]))

    while q:
        cost, cur, minGas = heapq.heappop(q)

        if visit[cur][minGas] < cost:
            continue

        for nxt, nw in path[cur].items():
            nextCost = cost + minGas * nw
            if nextCost < visit[nxt][minGas]:
                visit[nxt][minGas] = nextCost
                heapq.heappush(q, (nextCost, nxt, min(gas[nxt], minGas)))
    return visit[n]


print(min(dijkstra(1)))
