# https://www.acmicpc.net/problem/14938
import sys

read = sys.stdin.readline
n, m, r = map(int, read().strip().split())
items = list(map(int, read().strip().split()))
items.insert(0, 0)
dp = [[float('inf') if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, read().strip().split())
    dp[a][b] = c
    dp[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

ans = 0
for i in range(1, n + 1):
    ans = max(ans, sum(map(lambda x: items[x[0]], filter(lambda x: x[1] <= m, enumerate(dp[i])))))
print(ans)
