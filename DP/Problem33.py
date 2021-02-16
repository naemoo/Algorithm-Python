# https://www.acmicpc.net/problem/1234
import sys

read = sys.stdin.readline
n, r, g, b = map(int, read().strip().split())
dp = [[[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)] for _ in range(11)]
factorial = [1 for _ in range(11)]
for i in range(1, 11):
    factorial[i] = factorial[i - 1] * i


def make_tree(k, r, g, b):
    if r < 0 or g < 0 or b < 0:
        return float('inf')

    if k == n + 1:
        return 1

    if dp[k][r][g][b] != -1:
        return dp[k][r][g][b]

    ret = 0
    for i in range(1, 4):
        if k % i:
            continue
        num = k // i
        if i == 1:
            cnt = 1
            tmp = make_tree(k + 1, r - num, g, b)
            ret += tmp * cnt if tmp != float('inf') else 0
            tmp = make_tree(k + 1, r, g - num, b)
            ret += tmp * cnt if tmp != float('inf') else 0
            tmp = make_tree(k + 1, r, g, b - num)
            ret += tmp * cnt if tmp != float('inf') else 0
        elif i == 2:
            cnt = factorial[k] // (factorial[k // 2] ** 2)
            tmp = make_tree(k + 1, r - num, g - num, b)
            ret += tmp * cnt if tmp != float('inf') else 0
            tmp = make_tree(k + 1, r - num, g, b - num)
            ret += tmp * cnt if tmp != float('inf') else 0
            tmp = make_tree(k + 1, r, g - num, b - num)
            ret += tmp * cnt if tmp != float('inf') else 0
        else:
            cnt = factorial[k] // (factorial[k // 3] ** 3)
            tmp = make_tree(k + 1, r - num, g - num, b - num)
            ret += tmp * cnt if tmp != float('inf') else 0
    dp[k][r][g][b] = ret if ret else float('inf')
    return dp[k][r][g][b]


ans = make_tree(1, r, g, b)
print(ans if ans != float('inf') else 0)
