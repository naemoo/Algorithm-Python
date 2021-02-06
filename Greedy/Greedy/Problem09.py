# https://www.acmicpc.net/problem/3687
import sys

read = sys.stdin.readline
t = int(read().strip())
matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 6]


def getMin(l, n, num):
    global dp1
    if n == 0:
        dp1[l][n] = num
        return num

    if dp1[l][n] != -1:
        return dp1[l][n]

    ret = float('inf')
    for i in range(10):
        nxt = n - matches[i]
        if l == 0 and i == 0:
            continue

        if nxt >= 0:
            ret = min(getMin(l + 1, nxt, num * 10 + i), ret)
    dp1[l][n] = ret
    return ret


def getMax(l, n, num):
    global dp2
    if n == 0:
        dp2[l][n] = num
        return num

    if dp2[l][n] != -1:
        return dp2[l][n]

    ret = 0
    for i in range(9, -1, -1):
        nxt = n - matches[i]
        if l == 0 and i == 0:
            continue

        if nxt >= 0:
            ret = max(getMax(l + 1, nxt, num * 10 + i), ret)
    dp2[l][n] = ret
    return ret


while t:
    n = int(read().strip())
    dp1 = [[-1 for _ in range(101)] for _ in range(51)]
    getMin(0, n, 0)
    dp2 = [[-1 for _ in range(101)] for _ in range(51)]
    getMax(0, n, 0)
    print(dp1[0][n], dp2[0][n])
    t -= 1
