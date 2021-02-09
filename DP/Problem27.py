# https://www.acmicpc.net/problem/2342
import sys

sys.setrecursionlimit(10 ** 5 + 10)
read = sys.stdin.readline
cmd = list(map(int, read().strip().split()))
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(100001)]


def getCost(foot, direction):
    if foot:
        if foot == direction:
            return 1
        elif max(foot, direction) - min(foot, direction) == 2:
            return 4
        else:
            return 3
    else:
        return 2


def doGame(d, l, r):
    if d == len(cmd) - 1:
        return 0
    if dp[d][l][r] != -1:
        return dp[d][l][r]

    ret = float('inf')
    if cmd[d] != r:
        ret = doGame(d + 1, cmd[d], r) + getCost(l, cmd[d])
    if cmd[d] != l:
        ret = min(ret, doGame(d + 1, l, cmd[d]) + getCost(r, cmd[d]))
    dp[d][l][r] = ret
    return ret


print(doGame(0, 0, 0))
