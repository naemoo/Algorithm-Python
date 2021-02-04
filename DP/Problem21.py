# https://www.acmicpc.net/problem/5582
import sys

read = sys.stdin.readline
a = read().strip()
b = read().strip()
ret = 0
dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = 0
        ret = max(ret, dp[i][j])

print(ret)
