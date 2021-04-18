# https://www.acmicpc.net/problem/2662
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
invests = [list(map(int, read().strip().split())) for _ in range(n)]
invests.insert(0, 0)
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
track = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j]
        for e in range(1, j + 1):
            if dp[i - 1][j - e] + invests[e][i] > dp[i][j]:
                track[i][j] = e
                dp[i][j] = dp[i - 1][j - e] + invests[e][i]
ans = [0] * (m + 1)


def go(d, money):
    if d == 0 or money == 0:
        return
    ans[d] = track[d][money]
    go(d - 1, money - track[d][money])


print(dp[m][n])
go(m, n)
print(*ans[1:], sep=' ')
