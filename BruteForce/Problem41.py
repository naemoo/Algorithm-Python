# https://www.acmicpc.net/problem/14923
import sys
from collections import deque

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6 + 5)
n, m = map(int, read().strip().split())
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
hx, hy = map(int, read().strip().split())
ex, ey = map(int, read().strip().split())
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
graph = [list(map(int, read().strip().split())) for _ in range(n)]


def dfs(sx, sy):
    q = deque()
    q.append((sx, sy, 0, 0))
    visit[0][sx][sy] = True

    while q:
        x, y, wall, d = q.popleft()

        if (x, y) == (ex - 1, ey - 1):
            print(d)
            return

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[wall][nx][ny]:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny, wall, d + 1))
                visit[wall][nx][ny] = True
            elif wall == 0 and not visit[wall + 1][nx][ny]:
                q.append((nx, ny, wall + 1, d + 1))
                visit[wall][nx][ny] = True

    print(-1)
    return


dfs(hx - 1, hy - 1)
