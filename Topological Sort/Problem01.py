# https://www.acmicpc.net/problem/1766
import heapq
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
graph = defaultdict(list)
indegree = [0 for _ in range(n + 1)]
pq = []
ans = []

for _ in range(m):
    a, b = map(int, read().strip().split())
    indegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    tmp = heapq.heappop(pq)
    for nxt in graph[tmp]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(pq, nxt)
    ans.append(tmp)

for e in ans:
    print(e, end=' ')
