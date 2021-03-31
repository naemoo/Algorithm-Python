# https://www.acmicpc.net/problem/17182
import sys
from itertools import permutations

read = sys.stdin.readline
n, st = map(int, read().strip().split())
dp = [list(map(int, read().strip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = float('inf')
for cites in permutations(range(n), n):
    prev = st
    tmp = 0
    for city in cites:
        tmp += dp[prev][city]
        prev = city
    ans = min(ans, tmp)
print(ans)
