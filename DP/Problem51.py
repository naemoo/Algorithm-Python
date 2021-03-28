# https://www.acmicpc.net/problem/4811
import sys

read = sys.stdin.readline
dp = [[[-1 for _ in range(61)] for _ in range(31)] for _ in range(61)]


def go(d, w_cnt, h_cnt):
    if d == 2 * n:
        return 1
    if dp[d][w_cnt][h_cnt] != -1:
        return dp[d][w_cnt][h_cnt]

    ret = 0
    if w_cnt > 0:
        ret += go(d + 1, w_cnt - 1, h_cnt + 1)
    if h_cnt > 0:
        ret += go(d + 1, w_cnt, h_cnt - 1)
    dp[d][w_cnt][h_cnt] = ret
    return ret


while (n := int(read().strip())):
    print(go(0, n, 0))
