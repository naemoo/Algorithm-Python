# https://www.acmicpc.net/problem/1480
import sys

read = sys.stdin.readline
n, m, c = map(int, read().strip().split())
jewels = list(map(int, read().strip().split()))
dp = [[[-1 for _ in range(c + 1)] for _ in range(1 << 13)] for _ in range(m + 1)]


def getJewel(bags_num, state, capacity):
    if bags_num == m:
        return -1

    if dp[bags_num][state][capacity] != -1:
        return dp[bags_num][state][capacity]

    ret = 0
    for i in range(n):
        if state & (1 << i) == 0:
            nxt_w = capacity + jewels[i]
            nxt_state = state | (1 << i)
            if nxt_w <= c:
                ret = max(ret, getJewel(bags_num, nxt_state, nxt_w) + 1)
            elif jewels[i] <= c:
                ret = max(ret, getJewel(bags_num + 1, nxt_state, jewels[i]) + 1)
    dp[bags_num][state][capacity] = ret
    return ret


ans = getJewel(0, 0, 0)
print(ans)
