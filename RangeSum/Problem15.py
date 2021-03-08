# https://www.acmicpc.net/problem/2208
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
jewels = [int(read().strip()) for _ in range(n)]

p_sum = [0] * (n + 1)
for i in range(1, n + 1):
    p_sum[i] = p_sum[i - 1] + jewels[i - 1]

dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = min(dp[i - 1], p_sum[i])

ans = 0
for i in range(m, n + 1):
    ans = max(p_sum[i] - dp[i - m], ans)
print(ans)
