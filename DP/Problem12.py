# https://www.acmicpc.net/problem/5557
import sys

read = sys.stdin.readline
n = int(read().strip())
numbers = list(map(int, read().strip().split()))
dp = [[-1 for _ in range(21)] for _ in range(n)]


def go(d, num):
    if num < 0 or num > 20:
        return 0

    if d == n - 1:
        if num == numbers[n - 1]:
            return 1
        else:
            return 0

    if dp[d][num] != -1:
        return dp[d][num]

    ret = 0
    ret += go(d + 1, num + numbers[d])
    if d != 0:
        ret += go(d + 1, num - numbers[d])
    dp[d][num] = ret
    return ret


print(go(0, 0))
