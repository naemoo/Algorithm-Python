# https://www.acmicpc.net/problem/19238
import sys
from collections import deque

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m, fuel = map(int, read().strip().split())
maps = [list(map(int, read().strip().split())) for _ in range(n)]
start = tuple(map(lambda x: int(x) - 1, read().strip().split()))
passengers = dict()
for _ in range(m):
    sx, sy, ex, ey = map(int, read().strip().split())
    passengers[(sx - 1, sy - 1)] = (ex - 1, ey - 1)


def getDistance(cur, end):
    q = deque([[*cur, 0]])
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[cur[0]][cur[1]] = True
    if cur == end:
        return 0

    while q:
        x, y, d = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] or maps[nx][ny]:
                continue

            visit[nx][ny] = True
            nd = d + 1
            q.append((nx, ny, nd))

            if (nx, ny) == end:
                return nd
    return -1


# 갈때 소비 도착 소비 -> 도착 충전
def getCloser(cur):
    ret = []
    q = deque([[*cur, 0]])
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[cur[0]][cur[1]] = True
    if cur in passengers.keys():
        ret.append((*cur, 0))

    while q:
        x, y, d = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nd = d + 1

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny] or maps[nx][ny]:
                continue

            if (nx, ny) in passengers.keys():
                if ret and ret[-1][2] < nd:
                    return ret
                else:
                    ret.append((nx, ny, nd))

            visit[nx][ny] = True
            q.append((nx, ny, nd))
    return ret


while passengers:
    tmp = getCloser(start)
    tmp.sort(key=lambda x: (x[2], x[0], x[1]), reverse=True)
    if not tmp:
        fuel = -1
        break
    passenger = tmp.pop()
    # 목적지
    fuel -= passenger[2]
    if fuel < 0:
        break
    nxt = (passenger[0], passenger[1])
    distance = getDistance(nxt, passengers[nxt])
    if distance < 0:
        fuel = -1
        break
    fuel -= distance
    if fuel < 0:
        break
    fuel += distance * 2
    start = passengers[nxt]
    del passengers[nxt]

print(-1 if fuel < 0 else fuel)
