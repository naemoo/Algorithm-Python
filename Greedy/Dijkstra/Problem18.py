# https://www.acmicpc.net/problem/2665
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
n = int(read().strip())
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
maps = [list(map(int, read().strip())) for _ in range(n)]
visit = [[float('inf') for _ in range(n)] for _ in range(n)]
visit[0][0] = 0
q = [(0, 0, 0)]

while q:
    cost, x, y = heappop(q)

    if visit[x][y] < cost:
        continue

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        nxt_cost = cost if maps[nx][ny] else cost + 1

        if nxt_cost < visit[nx][ny]:
            heappush(q, (nxt_cost, nx, ny))
            visit[nx][ny] = nxt_cost

print(visit[n - 1][n - 1])
