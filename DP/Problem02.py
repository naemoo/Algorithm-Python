# https://www.acmicpc.net/problem/2294
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
coins = []
for _ in range(n):
    coins.append(int(read().strip()))
coins.sort()
dp = [float('inf')] * (k + 1)
dp[0] = 0
for i in range(n):
    for j in range(1, k + 1):
        if j - coins[i] >= 0:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
print(dp[k] if dp[k] != float('inf') else -1)
