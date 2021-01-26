# https://www.acmicpc.net/problem/1932
import sys

read = sys.stdin.readline
n = int(read().strip())

arr = [tuple(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def go(d, start):
    if d == n:
        return 0
    if dp[d][start] != -1:
        return dp[d][start]

    ret = 0
    ret = max(go(d + 1, start) + arr[d][start], ret)
    ret = max(go(d + 1, start + 1) + arr[d][start], ret)
    dp[d][start] = ret
    return ret


print(go(0, 0))
