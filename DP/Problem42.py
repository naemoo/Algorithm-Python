# https://www.acmicpc.net/problem/1937
import sys

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
sys.setrecursionlimit(2505)
n = int(read().strip())
forests = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
ans = 0


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    ret = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if forests[x][y] < forests[nx][ny]:
            ret = max(dfs(nx, ny) + 1, ret)
    dp[x][y] = ret
    return ret


for i, forest in enumerate(forests):
    for j, e in enumerate(forest):
        ans = max(ans, dfs(i, j))

print(ans)
