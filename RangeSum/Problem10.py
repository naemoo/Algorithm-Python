# https://www.acmicpc.net/problem/16973
import sys
from collections import deque

read = sys.stdin.readline
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
n, m = map(int, read().strip().split())
arr = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + arr[i - 1][j - 1] - dp[i - 1][j - 1]

h, w, sr, sc, fr, fc = map(int, read().strip().split())

q = deque()
q.append((sr, sc, 0))
visit = [[False for _ in range(m + 1)] for _ in range(n + 1)]
visit[sr][sc] = True
while q:
    x, y, depth = q.popleft()

    for dx, dy in direction:
        nx, ny, nd = x + dx, y + dy, depth + 1
        a, b, c, d = nx, ny, nx + h - 1, ny + w - 1

        if a < 1 or b < 1 or c > n or d > m or visit[nx][ny]:
            continue

        if not (dp[c][d] - dp[c][b - 1] - dp[a - 1][d] + dp[a - 1][b - 1]):
            q.append((nx, ny, nd))
            visit[nx][ny] = True
            if nx == fr and ny == fc:
                print(nd)
                sys.exit()
print(-1)
