# https://www.acmicpc.net/problem/14588
import sys

read = sys.stdin.readline
n = int(read().strip())
lines = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[float('inf') for _ in range(n)] for _ in range(n)]

for i, (px, py) in enumerate(lines):
    for j, (x, y) in enumerate(lines[i:], start=i):
        if i == j or y < px or py < x:
            continue
        dp[i][j] = 1
        dp[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

q = int(read().strip())
while q:
    a, b = map(int, read().strip().split())
    print(dp[a - 1][b - 1] if dp[a - 1][b - 1] != float('inf') else -1)
    q -= 1
