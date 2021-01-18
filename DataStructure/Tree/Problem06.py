# https://www.acmicpc.net/problem/11438
import sys
from collections import defaultdict, deque
from math import log

read = sys.stdin.readline
n = int(read().strip())
length = int(log(n, 2))
tree = defaultdict(list)
parent = [[0 for _ in range(length + 1)] for _ in range(n + 1)]
depth = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    st, to = map(int, read().strip().split())
    tree[st].append(to)
    tree[to].append(st)

q = deque()
q.append(1)
depth[1] = 0
while q:
    cur = q.popleft()
    for nxt in tree[cur]:
        if depth[nxt] == -1:
            q.append(nxt)
            parent[nxt][0] = cur
            depth[nxt] = depth[cur] + 1

for j in range(1, length + 1):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(length, -1, -1):
        diff = depth[b] - depth[a]
        if diff >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(length, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


m = int(read().strip())
while m:
    a, b = map(int, read().strip().split())
    print(lca(a, b))
    m -= 1
