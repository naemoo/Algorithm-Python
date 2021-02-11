# https://www.acmicpc.net/problem/12920
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
items = []
for _ in range(n):
    v, c, k = map(int, read().strip().split())
    for i in range(14):
        num = (1 << i)
        if k >= num:
            items.append((v * num, c * num))
            k -= num
            if k == 0:
                break
        else:
            items.append((v * k, c * k))
            break

items.sort()
dp = [[0 for _ in range(m + 1)] for _ in range(len(items))]

for i, item in enumerate(items):
    w, c = item
    for j in range(m + 1):
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + c)
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[len(dp) - 1][m])
