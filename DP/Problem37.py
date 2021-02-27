# https://www.acmicpc.net/problem/17845
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
classes = [tuple(map(int, read().strip().split())) for _ in range(k)]
classes.sort(key=lambda x: (x[1], x[0]))
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for i, e in enumerate(classes):
    i += 1
    for j in range(n + 1):
        if j - e[1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - e[1]] + e[0], dp[i - 1][j])
print(dp[k][n])

