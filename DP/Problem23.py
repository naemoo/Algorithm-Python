# https://www.acmicpc.net/problem/11062
import sys

read = sys.stdin.readline
t = int(read().strip())


def k_play(s, e):
    if e == s:
        return cards[e]

    if dp[s][e] != -1:
        return dp[s][e]

    ret = 0
    ret = m_play(s, e - 1) + cards[e]
    ret = max(ret, m_play(s + 1, e) + cards[s])
    dp[s][e] = ret
    return ret


def m_play(s, e):
    if e == s:
        return 0
    ret = 0
    ret = k_play(s, e - 1)
    ret = min(k_play(s + 1, e), ret)
    return ret


while t:
    n = int(read().strip())
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    cards = list(map(int, read().strip().split()))
    print(k_play(0, n - 1))
    t -= 1
