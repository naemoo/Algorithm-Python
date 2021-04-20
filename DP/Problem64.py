# https://www.acmicpc.net/problem/13302
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
days = set(map(lambda x: int(x) - 1, read().strip().split()))
dp = [[-1 for _ in range(40)] for _ in range(105)]


def go(d, c):
    if d >= n:
        return 0
    if dp[d][c] != -1:
        return dp[d][c]

    ret = float('inf')
    if d in days:
        ret = go(d + 1, c)
    else:
        nc = c if c < 3 else c - 3
        ret = min(ret, go(d + 1, nc) + (10000 if c < 3 else 0))
        ret = min(ret, go(d + 3, c + 1) + 25000)
        ret = min(ret, go(d + 5, c + 2) + 37000)
    dp[d][c] = ret
    return ret


print(go(0, 0))
