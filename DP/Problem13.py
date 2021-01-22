# https://www.acmicpc.net/problem/11726
import sys

read = sys.stdin.readline
n = int(read().strip())
dp = [-1 for _ in range(n + 1)]
if n <= 2:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10007)
