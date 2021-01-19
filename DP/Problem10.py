# https://www.acmicpc.net/problem/2602
import sys

read = sys.stdin.readline
ans = read().strip()
devil = read().strip()
angel = read().strip()
# 0 - angel 1 - devil
dp = [[[-1, -1] for _ in range(len(devil) + 1)] for _ in range(len(ans))]


def go(start, idx, isDevil=True):
    if idx == len(ans):
        return 1

    j = 1 if isDevil else 0
    if dp[idx][start][j] != -1:
        return dp[idx][start][j]

    ret = 0
    if isDevil:
        for i in range(start, len(devil)):
            if ans[idx] == devil[i]:
                ret += go(i + 1, idx + 1, False)
    else:
        for i in range(start, len(devil)):
            if ans[idx] == angel[i]:
                ret += go(i + 1, idx + 1, True)
    dp[idx][start][j] = ret
    for e in dp:
        print(e)
    print()
    return ret


go(0, 0)
go(0, 0, False)

print(sum(map(lambda x: sum(filter(lambda y: y > 0, x)), dp[0])))
