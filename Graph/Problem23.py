# https://www.acmicpc.net/problem/1719
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
paths = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

while m:
    a, b, c = map(int, read().strip().split())
    dp[a][b] = c
    dp[b][a] = c
    paths[a][b] = b
    paths[b][a] = a
    m -= 1

for i in range(1, n + 1):
    dp[i][i] = 0
    paths[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                paths[i][j] = paths[i][k]

for path in paths[1:]:
    for e in path[1:]:
        print(e if e != 0 else '-', end=' ')
    print()
