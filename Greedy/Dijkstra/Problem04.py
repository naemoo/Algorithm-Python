# https://www.acmicpc.net/problem/9370
import sys, heapq
from collections import defaultdict

inp = sys.stdin.readline
testCase = int(inp())


def dijkstra(start):
    q = [(0, start)]
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    while q:
        w, cur = heapq.heappop(q)

        if distance[cur] < w:
            continue

        if cur in graph.keys():
            for nxt, nw in graph[cur].items():
                nextWeight = nw + w
                if nextWeight < distance[nxt]:
                    heapq.heappush(q, (nextWeight, nxt))
                    distance[nxt] = nextWeight
    return distance


for _ in range(testCase):
    graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
    n, m, t = map(int, inp().split())
    start, g, h = map(int, inp().split())
    for _ in range(m):
        st, to, w = map(int, inp().split())
        graph[st][to] = w
        graph[to][st] = w
    destinations = [int(inp()) for _ in range(t)]
    graph[g][h] = graph[h][g] = graph[h][g] - 0.1
    distance = dijkstra(start)
    ans = []
    for des in destinations:
        if float == type(distance[des]) and distance[des] != float('inf'):
            ans.append(des)
    for i in sorted(ans):
        print(i,end=' ')
    print()