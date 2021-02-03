# https://www.acmicpc.net/problem/7579
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
apps = map(int, read().strip().split())
costs = map(int, read().strip().split())

apps = list(zip(costs, apps))
apps.sort()

dp = [[0 for _ in range(10001)] for _ in range(len(apps) + 1)]

for i in range(1, len(apps) + 1):
    for cost in range(10001):
        if cost - apps[i - 1][0] < 0:
            dp[i][cost] = dp[i - 1][cost]
        else:
            dp[i][cost] = max(dp[i - 1][cost - apps[i - 1][0]] + apps[i - 1][1], dp[i - 1][cost])

ret = float('inf')
for i, e in enumerate(dp[-1]):
    if e >= m:
        ret = min(ret, i)
print(ret)