# https://www.acmicpc.net/problem/1082
import sys

read = sys.stdin.readline
n = int(read().strip())
costs = [int(e) for e in read().strip().split()]
money = int(read().strip())

dp = [[-1 for _ in range(51)] for _ in range(51)]


def go(d, money, num):
    if money == 0:
        return num

    if dp[d][money] != -1:
        return dp[d][money]

    ret = 0
    for i in range(n - 1, -1, -1):
        nxt = money - costs[i]

        if i == 0 and d == 0:
            continue
        if nxt >= 0:
            tmp = num * 10 + i
            tmp = max(tmp, go(d + 1, nxt, tmp))
            ret = max(ret, tmp)

    dp[d][money] = ret
    return ret


go(0, money, 0)
print(dp[0][money])
