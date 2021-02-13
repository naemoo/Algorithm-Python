# https://www.acmicpc.net/problem/9328
import sys
from collections import deque, defaultdict

read = sys.stdin.readline
t = int(read().strip())
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def canGo(c, i, j):
    global ans
    if c == '.':
        return False
    elif c == '$':
        ans += 1
        return False
    elif c.isupper():
        if c.lower() in keys:
            return False
        else:
            doors[c.lower()].append((i, j))
            return True
    else:
        if c in keys:
            return False
        keys.add(c)
        for tx, ty in doors[c]:
            q.append((tx, ty))
            visit[tx][ty] = True
        doors[c].clear()
        return False


while t:
    h, w = map(int, read().strip().split())
    buildings = [read().strip() for _ in range(h)]
    keys = set(read().strip())
    doors = defaultdict(deque)
    q = deque()
    ans = 0
    visit = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        if buildings[i][0] != '*':
            if not canGo(buildings[i][0], i, 0):
                q.append((i, 0))
                visit[i][0] = True
        if buildings[i][-1] != '*':
            if not canGo(buildings[i][-1], i, w - 1):
                q.append((i, w - 1))
                visit[i][-1] = True
    for i in range(1, w - 1):
        if buildings[0][i] != '*':
            if not canGo(buildings[0][i], 0, i):
                q.append((0, i))
                visit[0][i] = True
        if buildings[-1][i] != '*':
            if not canGo(buildings[h - 1][i], h - 1, i):
                q.append((h - 1, i))
                visit[h - 1][i] = True

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w or visit[nx][ny] or buildings[nx][ny] == '*':
                continue
            if canGo(buildings[nx][ny], nx, ny):
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
    print(ans)
    t -= 1
