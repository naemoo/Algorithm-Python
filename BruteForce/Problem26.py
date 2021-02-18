# https://www.acmicpc.net/problem/5427
import sys
from collections import deque

read = sys.stdin.readline
t = int(read().strip())
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def spread_fire():
    global cur
    while fire_q and fire_q[0][2] <= cur:
        i, j, d = fire_q.popleft()

        for dx, dy in directions:
            ni, nj, ndp = i + dx, j + dy, d + 1
            if ni < 0 or nj < 0 or ni >= w or nj >= h:
                continue
            if buildings[ni][nj] == '.':
                fire_q.append((ni, nj, ndp))
                buildings[ni][nj] = '*'


while t:
    h, w = map(int, read().strip().split())
    buildings = [list(read().strip()) for _ in range(w)]
    visit = [[False for _ in range(h)] for _ in range(w)]

    fire_q = deque()
    s_q = deque()
    for i, building in enumerate(buildings):
        for j, e in enumerate(building):
            if e == '*':
                fire_q.append((i, j, 0))
            elif e == '@':
                buildings[i][j] = '.'
                s_q.append((i, j, 0))
    cur = -1
    isEnd = False
    while s_q:
        x, y, d = s_q.popleft()

        if isEnd:
            break
        if cur < d:
            cur += 1
            spread_fire()

        for dx, dy in directions:
            nx, ny, nd = x + dx, y + dy, d + 1

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                print(nd)
                isEnd = True
                break
            if visit[nx][ny]:
                continue
            if buildings[nx][ny] == '#' or buildings[nx][ny] == '*':
                continue
            s_q.append((nx, ny, nd))
            visit[nx][ny] = True
    if not isEnd:
        print('IMPOSSIBLE')
    t -= 1
