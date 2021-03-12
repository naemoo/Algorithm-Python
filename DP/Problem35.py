# https://www.acmicpc.net/problem/14728
import sys

read = sys.stdin.readline
n, t = map(int, read().strip().split())
tests = [tuple(map(int, read().strip().split())) for _ in range(n)]
tests.sort()
dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i, test in enumerate(tests):
    i += 1
    time, score = test
    for j in range(t + 1):
        if j - time < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + score)

print(dp[n][t])
