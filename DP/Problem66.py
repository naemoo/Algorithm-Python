# https://www.acmicpc.net/problem/2688
import sys

read = sys.stdin.readline
test = int(read().strip())
dp = [[-1 for _ in range(10)] for _ in range(70)]


def getCount(d, n):
    if d == 1:
        return 1
    if dp[d][n] != -1:
        return dp[d][n]

    ret = 0
    for i in range(n + 1):
        ret += getCount(d - 1, i)
    dp[d][n] = ret

    return ret


while test:
    n = int(read().strip())
    ans = 0
    for i in range(10):
        ans += getCount(n, i)
    print(ans)
    test -= 1
