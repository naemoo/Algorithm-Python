# https://www.acmicpc.net/problem/7569
import sys
from collections import deque

read = sys.stdin.readline
directions = ((0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))
m, n, height = map(int, read().strip().split())
tomatoes = [[list(map(int, read().strip().split())) for _ in range(n)] for _ in range(height)]
q = deque()
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(height)]

for h, tomato in enumerate(tomatoes):
    for i, (row) in enumerate(tomato):
        for j, e in enumerate(row):
            if e == 1:
                q.append((h, i, j, 0))
                visit[h][i][j] = True
            elif e == -1:
                visit[h][i][j] = True


while q:
    h, x, y, d = q.popleft()

    for dh, dx, dy in directions:
        nh, nx, ny = h + dh, x + dx, y + dy
        nd = d + 1

        if nh < 0 or nx < 0 or ny < 0 or nh >= height or nx >= n or ny >= m or visit[nh][nx][ny]:
            continue

        if tomatoes[nh][nx][ny] != 0:
            continue

        q.append((nh, nx, ny, nd))
        visit[nh][nx][ny] = True

for state in visit:
    for row in state:
        for e in row:
            if not e:
                print(-1)
                sys.exit()
print(d)

