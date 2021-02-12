# https://www.acmicpc.net/problem/2169
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
sys.setrecursionlimit(n * m + 5)
mars = [list(map(int, read().strip().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
dp = [[[-float('inf') for _ in range(m)] for _ in range(n)] for _ in range(3)]
visit[0][0] = True
# 0 왼 1 아래 2 오른
direction = ((0, -1), (1, 0), (0, 1))


def go(x, y, d):
    if x == n - 1 and y == n - 1:
        return mars[0][0]

    if dp[d][x][y] != -float('inf'):
        return dp[d][x][y]

    ret = -float('inf')
    for i in range(3):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny]:
            continue
        visit[nx][ny] = True
        ret = max(go(nx, ny, i) + mars[nx][ny], ret)
        visit[nx][ny] = False
    dp[d][x][y] = ret
    return ret

print(go(0, 0, 0))
