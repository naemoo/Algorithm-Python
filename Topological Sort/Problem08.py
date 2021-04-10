# https://www.acmicpc.net/problem/14676
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
adj = defaultdict(list)
indegree = [0] * (n + 1)
isBuilt = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    indegree[b] += 1

for _ in range(k):
    a, b = map(int, read().strip().split())
    if a - 1:
        if not isBuilt[b]:
            print('Lier!')
            sys.exit()
        isBuilt[b] -= 1
        if isBuilt[b] == 0:
            for nxt in adj[b]:
                indegree[nxt] += 1
    else:
        if indegree[b]:
            print('Lier!')
            sys.exit()
        isBuilt[b] += 1
        for nxt in adj[b]:
            indegree[nxt] -= 1
            indegree[nxt] = max(indegree[nxt], 0)

print('King-God-Emperor')
