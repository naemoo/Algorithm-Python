# https://www.acmicpc.net/problem/11437
import sys
from collections import defaultdict, deque
from math import log

read = sys.stdin.readline
n = int(read().strip())
maxH = int(log(n, 2))
adj = defaultdict(list)
for _ in range(n - 1):
    st, to = map(int, read().strip().split())
    adj[st].append(to)
    adj[to].append(st)
parent = [[0 for _ in range(maxH + 1)] for _ in range(n + 1)]
m = int(read().strip())
depth = [-1 for _ in range(n + 1)]

q = deque()
q.append(1)
visit = [False for _ in range(n + 1)]
visit[1] = visit
depth[1] = 0
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not visit[nxt]:
            q.append(nxt)
            visit[nxt] = True
            depth[nxt] = depth[cur] + 1
            parent[nxt][0] = cur


for j in range(1, maxH + 1):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(maxH, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a

    for i in range(maxH, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

while m:
    a, b = map(int, read().strip().split())
    print(lca(a, b))
    m -= 1
