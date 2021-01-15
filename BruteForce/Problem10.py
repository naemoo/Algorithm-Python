# https://www.acmicpc.net/problem/1103
import sys

read = sys.stdin.readline

n, m = map(int, read().strip().split())
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

games = [[int(e) if e != 'H' else -1 for e in list(read().strip())] for _ in range(n)]
visit = [[True for _ in range(m)] for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
visit[0][0] = False
ret = 0


def go(x, y, d):
    global ret
    ret = max(ret, d)
    dp[x][y] = max(d, dp[x][y])

    for dx, dy in direction:
        nx, ny, nd = x + dx * games[x][y], y + dy * games[x][y], d + 1
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                print(-1)
                sys.exit()

            if games[nx][ny] != -1 and dp[nx][ny] < nd:
                visit[nx][ny] = False
                go(nx, ny, nd)
                visit[nx][ny] = True

go(0, 0, 1)
print(ret)
