# https://www.acmicpc.net/problem/1761
import sys
from collections import defaultdict
from math import log

read = sys.stdin.readline
sys.setrecursionlimit(40006)
n = int(read().strip())
h = int(log(n, 2)) + 1
adj = defaultdict(list)

for _ in range(n - 1):
    a, b, c = map(int, read().strip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

parent = [[0 for _ in range(h)] for _ in range(n + 1)]
dist = [[0 for _ in range(h)] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]


def dfs(d, cur):
    depth[cur] = d

    for nxt, w in adj[cur]:
        if depth[nxt] == 0:
            dfs(d + 1, nxt)
            parent[nxt][0] = cur
            dist[nxt][0] = w


dfs(1, 1)

for j in range(1, h):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]
        dist[i][j] = dist[parent[i][j - 1]][j - 1] + dist[i][j - 1]


def lca(a, b):
    ret = 0
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(h - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            ret += dist[b][i]
            b = parent[b][i]

    if a == b:
        return ret

    for i in range(h - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            ret += (dist[a][i] + dist[b][i])
            a = parent[a][i]
            b = parent[b][i]
    ret += (dist[a][0] + dist[b][0])
    return ret


m = int(read().strip())
while m:
    a, b = map(int, read().strip().split())
    print(lca(a, b))
    m -= 1
