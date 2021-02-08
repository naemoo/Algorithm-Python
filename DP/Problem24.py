# https://www.acmicpc.net/problem/2098
import sys

read = sys.stdin.readline


def f(start, cities, dp):
    if dp[start][cities] != -1:
        return dp[start][cities]

    if cities == (1 << n) - 1:
        return w[start][0] if w[start][0] > 0 else float('inf')

    ret = float('inf')
    for i in range(1, n):
        if not ((cities >> i) & 1) and w[start][i] > 0:
            tmp = f(i, cities | (1 << i), dp)
            ret = min(tmp + w[start][i], ret)

    dp[start][cities] = ret
    return ret


n = int(read().strip())
w = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
print(f(0, 1, dp))
