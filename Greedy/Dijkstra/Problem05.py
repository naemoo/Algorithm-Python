# https://www.acmicpc.net/problem/1162
import heapq
import sys
from collections import defaultdict

inp = sys.stdin.readline
n, m, k = map(int, inp().strip().split())
roads = defaultdict(list)

for _ in range(m):
    st, to, w = map(int, inp().strip().split())
    roads[st].append((to,w))
    roads[to].append((st, w))

def dijkstra(start):
    q = [(0, start, 0)]
    length = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(len(length[start])):
        length[start][i] = 0

    while q:
        w, cur, ck = heapq.heappop(q)

        if length[cur][ck] < w:
            continue

        for nxt, nw in roads[cur]:
            if nw + w < length[nxt][ck]:
                heapq.heappush(q, (nw + w, nxt, ck))
                length[nxt][ck] = nw + w
            if ck < i and w < length[nxt][ck + 1]:
                heapq.heappush(q, (w, nxt, ck + 1))
                length[nxt][ck + 1] = w
    return length[n]

print(min(dijkstra(1)))
