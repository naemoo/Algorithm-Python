# https://www.acmicpc.net/problem/1956
import sys

read = sys.stdin.readline
v, e = map(int, read().strip().split())
dp = [[float('inf') for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, read().strip().split())
    dp[a][b] = c

for i in range(1, v + 1):
    dp[i][i] = 0

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = float('inf')
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            continue
        ans = min(ans, dp[i][j] + dp[j][i])
print(ans if ans != float('inf') else -1)
