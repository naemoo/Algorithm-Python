# https://www.acmicpc.net/problem/1648
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
dp = [[-1 for _ in range(1 << m)] for _ in range(n * m)]


def getAnswer(idx, state):
    if idx == n * m:
        return 0 if state else 1

    if dp[idx][state] != -1:
        return dp[idx][state]

    ret = 0
    if state & 1:
        ret += getAnswer(idx + 1, state >> 1)
    else:
        if idx % m < (m - 1) and not (state & 2):
            ret += getAnswer(idx + 2, state >> 2)
        ret += getAnswer(idx + 1, state >> 1 | (1 << (m - 1)))
    ret %= 9901
    dp[idx][state] = ret
    return ret


print(getAnswer(0, 0))
