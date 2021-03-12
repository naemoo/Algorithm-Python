# https://www.acmicpc.net/problem/17208
import sys

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
orders = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[[-1 for _ in range(301)] for _ in range(301)] for _ in range(101)]


def takeOrder(d, cheese, potato):
    if d == n:
        return 0

    if dp[d][cheese][potato] != -1:
        return dp[d][cheese][potato]
    ret = 0
    if cheese - orders[d][0] >= 0 and potato - orders[d][1] >= 0:
        ret = takeOrder(d + 1, cheese - orders[d][0], potato - orders[d][1]) + 1
    ret = max(takeOrder(d + 1, cheese, potato), ret)
    dp[d][cheese][potato] = ret
    return ret


ans = takeOrder(0, m, k)
print(ans)
