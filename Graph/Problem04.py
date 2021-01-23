# https://www.acmicpc.net/problem/11657
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(m):
    a, b, c = map(int, read().strip().split())
    adj[a][b] = min(adj[a][b], c)

visit = [float('inf') for _ in range(n + 1)]
visit[1] = 0

for _ in range(m - 1):
    for cur in adj.keys():
        for nxt, w in adj[cur].items():
            if visit[nxt] > w + visit[cur]:
                visit[nxt] = w + visit[cur]

isCycle = False
for cur in adj.keys():
    for nxt, w in adj[cur].items():
        if visit[nxt] > w + visit[cur]:
            isCycle = True
if isCycle:
    print(-1)
else:
    for i in range(2, n + 1):
        print(visit[i] if visit[i] != float('inf') else -1)
