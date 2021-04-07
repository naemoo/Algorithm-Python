# https://www.acmicpc.net/problem/15723
import sys
from re import split
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
dp = defaultdict(lambda: defaultdict(lambda: float('inf')))
logics = set()

for _ in range(n):
    a, b = split('\sis\s', read().strip())
    dp[a][b] = 1
    logics.add(a)
    logics.add(b)

for i in dp:
    dp[i][i] = 0

for k in logics:
    for i in logics:
        for j in logics:
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

m = int(read().strip())
for _ in range(m):
    a, b = split('\sis\s', read().strip())
    print('T' if dp[a][b] != float('inf') else 'F')
