# https://www.acmicpc.net/problem/17244
import sys
from collections import deque

read = sys.stdin.readline
m, n = map(int, read().strip().split())
houses = [list(read().strip()) for _ in range(n)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = deque()
stuff_loc = {}
cnt = 0

for i, house in enumerate(houses):
    for j, e in enumerate(house):
        if e == 'S':
            q.append((i, j, 0, 0))
        elif e == 'X':
            stuff_loc[(i, j)] = cnt
            cnt += 1

visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(1 << cnt)]
x, y, s, d = q[0]
visit[s][x][y] = 0
while q:
    x, y, s, d = q.popleft()

    if s == (1 << cnt) - 1 and houses[x][y] == 'E':
        print(d)
        sys.exit()

    for dx, dy in directions:
        nx, ny, nd = x + dx, y + dy, d + 1

        if nx < 0 or ny < 0 or nx >= n or ny >= m or houses[nx][ny] == '#' or visit[s][nx][ny]:
            continue

        ns = s | (1 << stuff_loc[(nx, ny)]) if houses[nx][ny] == 'X' else s
        if not visit[ns][nx][ny]:
            q.append((nx, ny, ns, nd))
            visit[ns][nx][ny] = True
