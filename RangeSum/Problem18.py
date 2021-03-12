# https://www.acmicpc.net/problem/3114
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
r, c = map(int, read().strip().split())
directions = ((1, 0), (0, 1), (1, 1))
farms = [read().strip().split() for _ in range(r)]
b_farms = list(map(lambda farm: list(map(lambda x: int(x[1:]) if 'B' in x else 0, farm)), farms))
a_farms = list(map(lambda farm: list(map(lambda x: int(x[1:]) if 'A' in x else 0, farm)), farms))

for i in range(r):
    a_farms[i].append(0)
    b_farms[i].append(0)
    for j in range(1, c):
        a_farms[i][j] += a_farms[i][j - 1]
        b_farms[i][c - j - 1] += b_farms[i][c - j]

dp = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if i == 0 or j == 0:
            if i == 0:
                dp[i][j] = b_farms[i][j + 1]
            else:
                dp[i][j] = dp[i - 1][j] + b_farms[i][j + 1]
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a_farms[i][j - 1] + b_farms[i][j + 1]
        dp[i][j] = max(dp[i][j], dp[i][j - 1] + b_farms[i][j + 1] - b_farms[i][j])
print(dp[r - 1][c - 1])
