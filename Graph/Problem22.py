# https://www.acmicpc.net/problem/10159
import sys

read = sys.stdin.readline
n = int(read().strip())
m = int(read().strip())
dp_r = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]
dp = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]

while m:
    a, b = map(lambda x: int(x) - 1, read().strip().split())
    dp[b][a] = 1
    dp_r[a][b] = 1
    m -= 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp_r[i][j] = min(dp_r[i][j], dp_r[i][k] + dp_r[k][j])

for i in range(n):
    tmp = 0
    for j in range(n):
        if dp_r[i][j] == float('inf') and dp[i][j] == float('inf'):
            tmp += 1
    print(tmp)
