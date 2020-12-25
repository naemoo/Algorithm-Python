# https://www.acmicpc.net/problem/4781
import sys
from decimal import Decimal

read = sys.stdin.readline
tmp = read().strip()

while tmp != '0 0.00':
    n, m = map(Decimal, tmp.split())
    n = int(n)
    m = int(m * 100)
    dp = [0] * (m + 1)
    candies = []
    for _ in range(n):
        c, p = map(Decimal, read().strip().split())
        c = int(c)
        p = int(p * 100)
        candies.append((c, p))

    candies.sort()

    for i in range(n):
        for j in range(m + 1):
            if candies[i][1] <= j:
                dp[j] = max(dp[j], dp[j - candies[i][1]] + candies[i][0])
    print(dp[m])
    tmp = read().strip()
