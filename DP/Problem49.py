# https://www.acmicpc.net/problem/2618
import sys

read = sys.stdin.readline
sys.setrecursionlimit(1100)
n = int(read().strip())
w = int(read().strip())
first, second = (1, 1), (n, n)
cases = [list(map(int, read().strip().split())) for _ in range(w)]
cases.insert(0, None)
dp = [[-1 for _ in range(1005)] for _ in range(1005)]


def police(start, end):
    d = max(start, end) + 1
    if d == w + 1:
        return 0

    if dp[start][end] != -1:
        return dp[start][end]

    x, y = cases[d]
    distA = abs(cases[start][0] - x) + abs(cases[start][1] - y) if start else abs(first[0] - x) + abs(first[1] - y)
    distB = abs(cases[end][0] - x) + abs(cases[end][1] - y) if end else abs(second[0] - x) + abs(second[1] - y)

    ret = min(police(d, end) + distA, police(start, d) + distB)
    dp[start][end] = ret
    return ret


def tracking(start, end):
    d = max(start, end) + 1
    if d == w + 1:
        return
    x, y = cases[d]
    distA = abs(cases[start][0] - x) + abs(cases[start][1] - y) if start else abs(first[0] - x) + abs(first[1] - y)
    distB = abs(cases[end][0] - x) + abs(cases[end][1] - y) if end else abs(second[0] - x) + abs(second[1] - y)

    tmp1 = police(d, end) + distA
    tmp2 = police(start, d) + distB

    if tmp1 < tmp2:
        tracking(d, end)
        logs.append(1)
    else:
        tracking(start, d)
        logs.append(2)


print(police(0, 0))
logs = []
tracking(0, 0)
while logs:
    print(logs.pop())
