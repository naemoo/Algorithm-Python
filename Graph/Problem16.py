# https://www.acmicpc.net/problem/2660
import sys

read = sys.stdin.readline
n = int(read().strip())
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0

while (e := tuple(map(int, read().strip().split()))) != (-1, -1):
    dp[e[0]][e[1]] = 1
    dp[e[1]][e[0]] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

score = float('inf')
chairman = []

for i, e in enumerate(dp[1:], start=1):
    tmp = max(e[1:])
    if tmp < score:
        score = tmp
        chairman = []
        chairman.append(i)
    elif tmp == score:
        chairman.append(i)

print(score, len(chairman))
print(*chairman,sep=' ')