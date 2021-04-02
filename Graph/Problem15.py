# https://www.acmicpc.net/problem/1613
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

while k:
    a, b = map(int, read().strip().split())
    dp[a][b] = 1
    k -= 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

s = int(read().strip())
while s:
    a, b = map(int, read().strip().split())
    if dp[a][b] != float('inf'):
        print(-1)
    elif dp[b][a] != float('inf'):
        print(1)
    else:
        print(0)

    s -= 1
