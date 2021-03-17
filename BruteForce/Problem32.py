# https://www.acmicpc.net/problem/2234
import sys
from collections import deque, defaultdict

read = sys.stdin.readline
m, n = map(int, read().strip().split())
castle = [list(map(int, read().strip().split())) for _ in range(n)]
visit = [[-1 for _ in range(m)] for _ in range(n)]
directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

ans = [0] * 3


def dfs(x, y, section):
    ret = 1

    for i, dir, in enumerate(directions):
        dx, dy = dir
        nx, ny = x + dx, y + dy
        if castle[x][y] & (1 << i):
            continue

        if visit[nx][ny] != -1:
            continue

        visit[nx][ny] = section
        ret += dfs(nx, ny, section)

    return ret


adj = defaultdict(set)
rooms = {}
for i in range(n):
    for j in range(m):
        if visit[i][j] == -1:
            visit[i][j] = ans[0]
            size = dfs(i, j, ans[0])
            ans[1] = max(ans[1], size)
            rooms[ans[0]] = size
            ans[0] += 1

for i in range(n):
    for j in range(m):
        for dx, dy in directions:
            ny = j + dy
            nx = i + dx
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[i][j] == visit[nx][ny]:
                continue
            adj[visit[i][j]].add(visit[nx][ny])

for cur in adj:
    for nxt in adj[cur]:
        ans[2] = max(ans[2], rooms[nxt] + rooms[cur])

for e in ans:
    print(e)
