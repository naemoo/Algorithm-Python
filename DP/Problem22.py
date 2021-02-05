# https://www.acmicpc.net/problem/9252
import sys

read = sys.stdin.readline
a = read().strip()
b = read().strip()

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
track = [[None for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
ans = []

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            track[i][j] = (i - 1, j - 1)
        else:
            tmp1 = dp[i - 1][j]
            tmp2 = dp[i][j - 1]
            if tmp1 >= tmp2:
                track[i][j] = (i - 1, j)
            else:
                track[i][j] = (i, j - 1)
            dp[i][j] = max(tmp1, tmp2)


def tracking(i, j):
    if i <= 0 or j <= 0:
        return
    if a[i - 1] == b[j - 1]:
        ans.append(a[i - 1])
    if track[i][j]:
        x, y = track[i][j]
        tracking(x, y)


tracking(len(a), len(b))
tmp = dp[len(a)][len(b)]
print(tmp)
if tmp:
    ans.reverse()
    print("".join(ans))
