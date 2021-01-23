# https://www.acmicpc.net/problem/11051
import sys

read = sys.stdin.readline

t = int(read().strip())

dp = [[0 for _ in range(31)] for _ in range(31)]

for i in range(1, 31):
    for j in range(0, 31):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

while t:
    n, m = map(int, read().strip().split())
    print(dp[m][n])
    t -= 1
