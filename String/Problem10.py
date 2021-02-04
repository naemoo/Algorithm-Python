# https://www.acmicpc.net/problem/1256
import sys

read = sys.stdin.readline
dp = [[-1 for _ in range(201)] for _ in range(201)]
dp[1][1], dp[1][0] = 1, 1

for i in range(1, 201):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]


def go(ans, a, z):
    global k, n, m

    if a == n or z == m:
        for _ in range(n - a):
            ans += 'a'
        for _ in range(m - z):
            ans += 'z'
        print(ans)
        sys.exit()

    total = n + m - a - z
    left = dp[total - 1][n - a - 1]
    if k <= left:
        go(ans + 'a', a + 1, z)
    else:
        k -= left
        go(ans + 'z', a, z + 1)


n, m, k = map(int, read().strip().split())
if dp[n + m][n] < k:
    print(-1)
    sys.exit()
go('', 0, 0)
