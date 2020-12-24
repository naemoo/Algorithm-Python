# https://www.acmicpc.net/problem/2293
import sys

read = sys.stdin.readline
n,k = map(int,read().strip().split())
coins = []
for _ in range(n):
    coins.append(int(read().strip()))

dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    for j in range(1,k+1):
        if j - coins[i] >= 0:
            dp[j] += dp[j - coins[i]]
print(dp[k])





