# https://www.acmicpc.net/problem/2624
import sys

read = sys.stdin.readline
t = int(read().strip())
n = int(read().strip())
coins = []
for _ in range(n):
    coins.append(tuple(map(int, read().strip().split())))
coins.sort()

dp = [[0] * (t + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(len(coins)):
    coin, num = coins[i]
    i += 1
    for j in range(t + 1):

        if j < coin:
            dp[i][j] = dp[i - 1][j]
            continue

        for k in range(num + 1):
            if j - coin * k >= 0:
                dp[i][j] += dp[i - 1][j - k * coin]

print(dp[n][t])
