# https://www.acmicpc.net/problem/10937
import sys

read = sys.stdin.readline
n = int(read().strip())
prices = {'AA': 100, 'AB': 70, 'AC': 40, 'AF': 0,
          'BA': 70, 'BB': 50, 'BC': 30, 'BF': 0,
          'CA': 40, 'CB': 30, 'CC': 20, 'CF': 0,
          'FA': 0, 'FB': 0, 'FC': 0, 'FF': 0}
tofu = [read().strip() for _ in range(n)]
dp = [[None for _ in range(1 << n)] for _ in range(n * n)]


def getPrice(idx, state):
    if idx == n * n:
        return 0

    if dp[idx][state]:
        return dp[idx][state]

    ret = 0
    r, c = idx // n, idx % n
    if state & 1:
        ret = getPrice(idx + 1, state >> 1)
    else:
        ret = getPrice(idx + 1, state >> 1)
        if c + 1 < n and not state & 2:
            ret = max(ret, getPrice(idx + 2, state >> 2) + prices[tofu[r][c] + tofu[r][c + 1]])
        if r + 1 < n:
            ret = max(ret, getPrice(idx + 1, state >> 1 | (1 << (n - 1))) + prices[tofu[r][c] + tofu[r + 1][c]])
    dp[idx][state] = ret
    return ret


print(getPrice(0, 0))
