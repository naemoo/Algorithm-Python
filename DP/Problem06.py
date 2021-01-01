# https://www.acmicpc.net/problem/11404
import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline

n = int(read().strip())
m = int(read().strip())
buses = defaultdict(list)

for _ in range(m):
    st, to, w = map(int, read().strip().split())
    buses[st - 1].append((to - 1, w))


def dijkstra(start):
    q = [(0, start)]
    visit = [float('inf')] * n
    visit[start] = 0

    while q:
        w, cur = heapq.heappop(q)

        if visit[cur] < w:
            continue

        for nxt, nw in buses[cur]:
            nextCost = nw + w
            if nextCost < visit[nxt]:
                heapq.heappush(q, (nextCost, nxt))
                visit[nxt] = nextCost
    return visit


for start in range(n):
    for e in dijkstra(start):
        print(e if e != float('inf') else 0, end=' ')
    print()
