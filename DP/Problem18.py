# https://www.acmicpc.net/problem/2579
import sys

read = sys.stdin.readline
n = int(read().strip())
stairs = [int(read().strip()) for _ in range(n)]
dp = [0 for _ in range(n)]
if n == 1:
    print(stairs[0])
    sys.exit()
if n == 2:
    print(stairs[1] + stairs[0])
    sys.exit()
dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]
dp[2] = max(stairs[2] + stairs[1], stairs[0] + stairs[2])
for i in range(3, n):
    dp[i] = max(dp[i - 2] + stairs[i], stairs[i - 1] + stairs[i] + dp[i - 3])
print(dp[n - 1])
