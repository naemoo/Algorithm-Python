# https://www.acmicpc.net/problem/3055
import sys
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
read = sys.stdin.readline
r, c = map(int, read().strip().split())
visit = [[True for _ in range(c)] for _ in range(r)]
forest = []
waterQ = deque()
q = deque()

for i in range(r):
    forest.append(list(read().strip()))
    for j, e in enumerate(forest[i]):
        if e == '*':
            waterQ.append((i, j, 0))
            visit[i][j] = False
        elif e == 'S':
            q.append((i, j, 0))
            visit[i][j] = False
            visit[i][j] = '.'


def spreadWater(cur):
    while waterQ and waterQ[0][2] <= cur:
        x, y, d = waterQ.popleft()

        for dx, dy in directions:
            nx, ny, nd = x + dx, y + dy, d + 1

            if 0 <= nx < r and 0 <= ny < c:
                if visit[nx][ny] and forest[nx][ny] == '.':
                    waterQ.append((nx, ny, nd))
                    visit[nx][ny] = False


def getMin(forest):
    cur = -1

    while q:
        x, y, d = q.popleft()
        if cur < d:
            spreadWater(d)
            cur = d

        for dx, dy in directions:
            nx, ny, nd = x + dx, y + dy, d + 1

            if 0 <= nx < r and 0 <= ny < c:
                if visit[nx][ny] and forest[nx][ny] == '.':
                    q.append((nx, ny, nd))
                    visit[nx][ny] = False
                if forest[nx][ny] == 'D':
                    return nd


ans = getMin(forest)
print(ans if ans != None else "KAKTUS")
