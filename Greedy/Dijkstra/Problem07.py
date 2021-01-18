# https://www.acmicpc.net/problem/1261
import heapq
import sys

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
read = sys.stdin.readline
n, m = map(int, read().strip().split())
maze = [[e for e in map(int, list(read().strip()))] for _ in range(m)]

q = [(0, 0, 0)]
length = [[float('inf')] * n for _ in range(m)]
length[0][0] = 0

while q:
    w, x, y = heapq.heappop(q)

    if length[x][y] < w:
        continue

    for dx, dy in d:
        nw = w
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if maze[nx][ny] == 1:
                nw += 1
            if nw < length[nx][ny]:
                heapq.heappush(q,(nw, nx, ny))
                length[nx][ny] = nw
print(length[m - 1][n - 1])
