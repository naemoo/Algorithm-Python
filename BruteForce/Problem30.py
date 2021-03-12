# https://www.acmicpc.net/problem/1194
import sys
from collections import deque

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
read = sys.stdin.readline
r, c = map(int, read().strip().split())
mazes = [list(read().strip()) for _ in range(r)]
visit = [[[False for _ in range(c)] for _ in range(r)] for _ in range(64)]
key = 0
q = deque()
A = ord('A')

for i, maze in enumerate(mazes):
    for j, e in enumerate(maze):
        if e == '0':
            maze[j] = '.'
            q.append((i, j, key, 0))
            visit[key][i][j] = True

while q:
    x, y, k, d = q.popleft()

    for dx, dy in directions:
        nx, ny, nd = x + dx, y + dy, d + 1

        if nx < 0 or ny < 0 or nx >= r or ny >= c or visit[k][nx][ny]:
            continue
        nk = k
        e = mazes[nx][ny]
        if e == '#':
            continue
        elif e == '.':
            q.append((nx, ny, nk, nd))
            visit[nk][nx][ny] = True
        elif e.isalpha():
            if e.isupper():
                if k & (1 << (ord(e) - A)):
                    q.append((nx, ny, nk, nd))
                    visit[nk][nx][ny] = True
            else:
                nk |= 1 << (ord(e.upper()) - A)
                q.append((nx, ny, nk, nd))
                visit[nk][nx][ny] = True
        elif e == '1':
            print(nd)
            sys.exit()
print(-1)