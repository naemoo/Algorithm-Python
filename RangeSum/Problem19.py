# https://www.acmicpc.net/problem/13398
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = list(map(int, read().strip().split()))
dp = [[-float('inf')] * 2 for _ in range(n + 1)]
ans = -float('inf')

for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0] + arr[i - 1], arr[i - 1])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i - 1])
    ans = max(*dp[i], ans)

print(ans)
