# https://www.acmicpc.net/problem/2515
import sys
from bisect import bisect_left

sys.setrecursionlimit(300005)
read = sys.stdin.readline
n, s = map(int, read().strip().split())
paints = [list(map(int, read().strip().split())) for _ in range(n)]
paints.sort()
heights = list(map(lambda x: x[0], paints))
dp = [-1 for _ in range(n)]


def go(d):
    if d >= n:
        return 0

    if dp[d] != -1:
        return dp[d]

    ret = max(go(d + 1), go(bisect_left(heights, heights[d] + s)) + paints[d][1])
    dp[d] = ret
    return ret


print(go(0))
