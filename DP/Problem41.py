# https://www.acmicpc.net/problem/18427
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n, m, h = map(int, read().strip().split())
MOD = 10007
blocks = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(1001)] for _ in range(51)]


def go(d, height):
    if d == n:
        return 1 if height == h else 0

    if height > h:
        return 0

    if dp[d][height] != -1:
        return dp[d][height]

    ret = 0
    ret = (ret + go(d + 1, height)) % MOD
    for block in blocks[d]:
        ret = (ret + go(d + 1, height + block)) % MOD

    dp[d][height] = ret
    return ret


print(go(0, 0))
