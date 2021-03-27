# https://www.acmicpc.net/problem/1563
import sys

read = sys.stdin.readline
sys.setrecursionlimit(1005)
n = int(read().strip())
dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]
MOD = 1000000


def go(d, a_cnt, l_cnt):
    if d == n:
        return 1
    if dp[d][a_cnt][l_cnt] != -1:
        return dp[d][a_cnt][l_cnt]
    ret = 0
    ret = (ret + go(d + 1, 0, l_cnt)) % MOD
    if a_cnt < 2:
        ret = (ret + go(d + 1, a_cnt + 1, l_cnt)) % MOD
    if l_cnt == 0:
        ret = (ret + go(d + 1, 0, l_cnt + 1)) % MOD
    dp[d][a_cnt][l_cnt] = ret
    return ret


print(go(0, 0, 0))
