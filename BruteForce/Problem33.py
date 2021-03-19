# https://www.acmicpc.net/problem/11084
import sys
from collections import deque

read = sys.stdin.readline
r, c = map(int, read().strip().split())
directions = ((-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1), (1, -2), (2, -1))
MOD = 1000000009

visit = [[float('inf') for _ in range(c + 1)] for _ in range(r + 1)]
counts = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
counts[1][1] = 1
visit[1][1] = 0
q = deque()
q.append((1, 1, 0))

while q:
    x, y, d = q.popleft()

    for dx, dy in directions:
        nx, ny, nd = x + dx, y + dy, d + 1

        if nx <= 0 or ny <= 0 or nx > r or ny > c:
            continue

        if nd < visit[nx][ny]:
            counts[nx][ny] = counts[x][y]
            visit[nx][ny] = nd
            q.append((nx, ny, nd))
        elif nd == visit[nx][ny]:
            counts[nx][ny] = (counts[nx][ny] + counts[x][y]) % MOD

if visit[r][c] != float('inf'):
    print(visit[r][c], counts[r][c])
else:
    print('None')

