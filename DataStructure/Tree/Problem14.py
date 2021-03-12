# https://www.acmicpc.net/problem/3176
import sys
from collections import defaultdict, deque
from math import log

read = sys.stdin.readline
n = int(read().strip())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
for _ in range(n - 1):
    a, b, c = map(int, read().strip().split())
    adj[a][b] = c
    adj[b][a] = c

np = int(log(n) // log(2)) + 1
depth = [0 for _ in range(n + 1)]
parent = [[0 for _ in range(np)] for _ in range(n + 1)]
pMax = [[-1 for _ in range(np)] for _ in range(n + 1)]
pMin = [[float('inf') for _ in range(np)] for _ in range(n + 1)]

q = deque()
q.append(1)
depth[1] = 1
while q:
    cur = q.popleft()
    for nxt, w in adj[cur].items():
        if not depth[nxt]:
            depth[nxt] = depth[cur] + 1
            parent[nxt][0] = cur
            pMax[nxt][0] = w
            pMin[nxt][0] = w
            q.append(nxt)

for j in range(1, np):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]
        pMax[i][j] = max(pMax[parent[i][j - 1]][j - 1], pMax[i][j - 1])
        pMin[i][j] = min(pMin[parent[i][j - 1]][j - 1], pMin[i][j - 1])


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    rMax = -1
    rMin = float('inf')

    for i in range(np - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            rMax = max(rMax, pMax[b][i])
            rMin = min(rMin, pMin[b][i])
            b = parent[b][i]

    if a == b:
        return (rMin, rMax)

    for i in range(np - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            rMin = min(rMin, pMin[a][i], pMin[b][i])
            rMax = max(rMax, pMax[a][i], pMax[b][i])
            a = parent[a][i]
            b = parent[b][i]

    rMin = min(rMin, pMin[a][0], pMin[b][0])
    rMax = max(rMax, pMax[a][0], pMax[b][0])
    return (rMin, rMax)


k = int(read().strip())

while k:
    a, b = map(int, read().strip().split())
    print(*lca(a, b))
    k -= 1
