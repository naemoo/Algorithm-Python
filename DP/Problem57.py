# https://www.acmicpc.net/problem/1311
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]


def dfs(d, state):
    if d == n:
        return 0
    if dp[d][state] != -1:
        return dp[d][state]

    ret = float('inf')
    for i in range(n):
        if state & (1 << i) == 0:
            ret = min(ret, dfs(d + 1, state | (1 << i)) + arr[d][i])
    dp[d][state] = ret
    return ret


print(dfs(0, 0))
