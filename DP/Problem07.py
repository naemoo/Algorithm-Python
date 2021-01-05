# https://www.acmicpc.net/problem/1915
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, list(read().strip()))))

dp = [[0] * m for _ in range(n)]

ret = 0
for i in range(m):
    dp[0][i] = arr[0][i]
    ret = max(ret, dp[0][i])
for i in range(n):
    dp[i][0] = arr[i][0]
    ret = max(ret, dp[i][0])

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] != 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            ret = max(ret, dp[i][j])

print(ret ** 2)
