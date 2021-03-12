# https://www.acmicpc.net/problem/1486
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

n, m, t, d = map(int, read().strip().split())
maps = [read().strip() for _ in range(n)]
maps = list(map(lambda x: list(map(lambda y: ord(y) - ord('a') + 26 if y.islower() else ord(y) - ord('A'), x)), maps))
candidates = []


def dijkstra():
    q = []
    heappush(q, (0, 0, 0))
    visit = [[float('inf') for _ in range(m)] for _ in range(n)]
    visit[0][0] = 0
    while q:
        time, x, y = heappop(q)
        h = maps[x][y]
        if visit[x][y] < time:
            continue

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if abs(maps[nx][ny] - h) > t:
                continue

            nxtTime = time + (pow(maps[nx][ny] - h, 2) if maps[nx][ny] > h else 1)
            if nxtTime < visit[nx][ny]:
                heappush(q, (nxtTime, nx, ny))
                visit[nx][ny] = nxtTime
    return visit


def dijkstra2():
    q = []
    heappush(q, (0, 0, 0))
    visit = [[float('inf') for _ in range(m)] for _ in range(n)]
    visit[0][0] = 0

    while q:
        time, x, y = heappop(q)
        h = maps[x][y]
        if visit[x][y] < time:
            pass

        for dx, dy in direction:
            nx, ny = dx + x, dy + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if abs(maps[nx][ny] - h) > t:
                continue

            nxtTime = time + (pow(maps[nx][ny] - h, 2) if maps[nx][ny] < h else 1)
            if nxtTime < visit[nx][ny]:
                heappush(q, (nxtTime, nx, ny))
                visit[nx][ny] = nxtTime
    return visit


st_to = dijkstra()
to_st = dijkstra2()
ans = 0
for i in range(n):
    for j in range(m):
        if st_to[i][j] + to_st[i][j] <= d:
            ans = max(ans, maps[i][j])
print(ans)