# https://www.acmicpc.net/problem/11404
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
m = int(read().strip())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))

while m:
    a, b, w = map(int, read().strip().split())
    adj[a][b] = min(adj[a][b], w)
    m -= 1

dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
    for nxt, w in adj[i].items():
        dp[i][nxt] = w

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dp[i][j] if dp[i][j] != float('inf') else 0, end=' ')
    print()
