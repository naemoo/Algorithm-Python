# https://www.acmicpc.net/problem/1562
import sys

read = sys.stdin.readline
n = int(read().strip())
MOD = 1000000000
dp = [[[-1 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]


def go(d, num, state):
    global n
    if d == n:
        return 1 if state == 1023 else 0
    if dp[d][num][state] != -1:
        return dp[d][num][state]

    ret = 0
    if num + 1 < 10:
        ret = (ret + go(d + 1, num + 1, state | (1 << (num + 1)))) % MOD
    if num - 1 >= 0:
        ret = (ret + go(d + 1, num - 1, state | (1 << (num - 1)))) % MOD
    dp[d][num][state] = ret
    return ret


ans = 0
for i in range(1, 10):
    ans = (ans + go(1, i, 1 << i)) % MOD

print(ans)
