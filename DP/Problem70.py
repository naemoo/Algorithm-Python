# https://www.acmicpc.net/problem/1657
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
prices = {'AA': 10, 'AB': 8, 'AC': 7, 'AD': 5, 'AF': 1,
          'BA': 8, 'BB': 6, 'BC': 4, 'BD': 3, 'BF': 1,
          'CA': 7, 'CB': 4, 'CC': 3, 'CD': 2, 'CF': 1,
          'DA': 5, 'DB': 3, 'DC': 2, 'DD': 2, 'DF': 1,
          'FA': 1, 'FB': 1, 'FC': 1, 'FD': 1, 'FF': 0}
tofu = [list(read().strip()) for _ in range(n)]
dp = [[None for _ in range(1 << m)] for _ in range(n * m)]


def getPrice(idx, state):
    if idx == n * m:
        return 0

    if dp[idx][state]:
        return dp[idx][state]

    ret = 0
    x, y = idx // m, idx % m
    if state & 1:
        ret = getPrice(idx + 1, state >> 1)
    else:
        ret = getPrice(idx + 1, state >> 1)
        if y + 1 < m and not (state & 2):
            ret = max(ret, getPrice(idx + 2, (state >> 2)) + prices[tofu[x][y] + tofu[x][y + 1]])
        if x + 1 < n:
            ret = max(ret, getPrice(idx + 1, (state >> 1) | (1 << (m - 1))) + prices[tofu[x][y] + tofu[x + 1][y]])
    dp[idx][state] = ret
    return ret


print(getPrice(0, 0))
