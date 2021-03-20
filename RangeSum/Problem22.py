# https://www.acmicpc.net/problem/1749
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]


def getArea(a, b, h, w):
    c, d = a + h, b + w
    return dp[c][d] - dp[c][b] - dp[a][d] + dp[a][b]


ans = -float('inf')
for h in range(1, n + 1):
    for w in range(1, m + 1):
        for i in range(n - h + 1):
            for j in range(m - w + 1):
                ans = max(ans, getArea(i, j, h, w))

print(ans)
