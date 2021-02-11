# https://www.acmicpc.net/problem/4485
import heapq
import sys

read = sys.stdin.readline
n = int(read().strip())
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
t = 1
while n:
    games = [list(map(int, read().strip().split())) for _ in range(n)]
    q = []
    heapq.heappush(q, (games[0][0], 0, 0))
    visit = [[float('inf') for _ in range(n)] for _ in range(n)]
    visit[0][0] = games[0][0]

    while q:
        cost, x, y = heapq.heappop(q)

        if visit[x][y] < cost:
            continue

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nxtCost = cost + games[nx][ny]
                if nxtCost < visit[nx][ny]:
                    heapq.heappush(q, (nxtCost, nx, ny))
                    visit[nx][ny] = nxtCost
    print("Problem %d: %d" % (t, visit[n - 1][n - 1]))
    t += 1
    n = int(read().strip())
