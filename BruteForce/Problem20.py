# https://www.acmicpc.net/problem/5213
import sys
from collections import deque, defaultdict

read = sys.stdin.readline
n = int(read().strip())
bridges = [[-1 for _ in range(n * 2)] for _ in range(n)]
adj = defaultdict(list)
direction = ((1, 0), (-1, 0), (0, -1), (0, 1))

for i in range(n):
    if i % 2:
        for j in range(n - 1):
            a, b = map(int, read().strip().split())
            bridges[i][j * 2 + 1] = a
            bridges[i][j * 2 + 2] = b
    else:
        for j in range(n):
            a, b = map(int, read().strip().split())
            bridges[i][j * 2] = a
            bridges[i][j * 2 + 1] = b

tile_nums = [[None for _ in range(2 * n)] for _ in range(n)]
for row in range(n):
    for col in range(2 * n):
        if bridges[row][col] != -1:
            if row % 2 == 0:
                tile_nums[row][col] = (row - row // 2) * n + (row // 2) * (n - 1) + (col // 2 + 1)
            else:
                tile_nums[row][col] = (row - row // 2) * n + (row // 2) * (n - 1) + ((col - 1) // 2 + 1)
max_tile = tile_nums[-1][-2]
for x in range(n):
    for y in range(2 * n):
        now = tile_nums[x][y]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= 2 * n:
                continue
            nxt = tile_nums[nx][ny]
            if now != nxt and bridges[x][y] == bridges[nx][ny]:
                adj[now].append(nxt)


def trace_track(track, t):
    ans = []
    l = -1
    ans.append(t)
    while track[t]:
        ans.append(track[t])
        t = track[t]
    while ans:
        cur = ans.pop()
        if l != cur:
            print(cur, end=' ')
        l = cur


q = deque()
q.append((1, 1))
visit = [False for _ in range(max_tile + 1)]
path = [0 for _ in range(max_tile + 1)]
depth = [0 for _ in range(max_tile + 1)]
depth[1] = 1
visit[1] = True
flag = True
while q:
    cur, d = q.popleft()

    for nxt in adj[cur]:
        if visit[nxt]:
            continue
        visit[nxt] = True
        path[nxt] = cur
        depth[nxt] = d + 1
        q.append((nxt, d + 1))

        if nxt == max_tile:
            flag = False
            print(d + 1)
            trace_track(path, nxt)
if flag:
    for i in range(max_tile, -1, -1):
        if path[i]:
            print(depth[i])
            trace_track(path, i)
            sys.exit()
print(1)
print(1)
