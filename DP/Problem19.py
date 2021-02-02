# https://www.acmicpc.net/problem/11049
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [tuple(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def mul(a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    if a == b:
        return 0

    ret = float('inf')
    for k in range(a, b):
        ret = min(ret, mul(a, k) + mul(k + 1, b) + arr[a][0] * arr[k][1] * arr[b][1])
    dp[a][b] = ret
    return ret

print(mul(0, n - 1))
