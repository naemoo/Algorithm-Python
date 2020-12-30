# https://www.acmicpc.net/problem/12865
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())

stuff = []
for _ in range(n):
    w, v = map(int, read().strip().split())
    stuff.append((w, v))

stuff.sort()
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    w, v = stuff[i]
    i += 1
    for j in range(k + 1):
        if w <= j:
            dp[i][j] = dp[i - 1][j - w] + v
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
print(dp[n][k])