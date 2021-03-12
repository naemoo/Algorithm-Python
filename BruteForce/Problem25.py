# https://www.acmicpc.net/problem/1175
import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
classes = [list(read().strip()) for _ in range(n)]
cnt = 0
for i, e in enumerate(classes):
    for j, e in enumerate(e):
        if 'S' == e:
            x, y = i, j
        elif 'C' == e:
            if cnt == 1:
                classes[i][j] = 'D'
            cnt += 1

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
visit = [[[[[False for _ in range(m)] for _ in range(n)] for _ in range(4)] for _ in range(2)] for _ in range(2)]
q = deque()
for i in range(4):
    visit[0][0][i][x][y] = True
    q.append((i, x, y, 0, 0, 0, 0))

while q:
    direction, x, y, d, cnt, is_c_visit, is_d_visit = q.popleft()

    for n_dir, dir in enumerate(directions):
        nx, ny = x + dir[0], y + dir[1]
        n_cnt = cnt
        is_nc_visit = is_c_visit
        is_nd_visit = is_d_visit

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[is_nc_visit][is_nd_visit][n_dir][nx][
            ny] or n_dir == direction:
            continue

        if classes[nx][ny] == '#':
            continue
        if classes[nx][ny] == 'C':
            is_nc_visit = 1
        if classes[nx][ny] == 'D':
            is_nd_visit = 1
        q.append((n_dir, nx, ny, d + 1, n_cnt, is_nc_visit, is_nd_visit))
        visit[is_nc_visit][is_nd_visit][n_dir][nx][ny] = True
        if is_nc_visit & is_nd_visit:
            print(d + 1)
            sys.exit()
print(-1)
