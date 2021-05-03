# https://www.acmicpc.net/problem/17144
import sys
from copy import deepcopy

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c, t, = map(int, read().strip().split())
dirties = [list(map(int, read().strip().split())) for _ in range(r)]
purifier = []
for i in range(r):
    if dirties[i][0] == -1:
        purifier.append(i)


def spreadDirt():
    ret = deepcopy(dirties)

    for x in range(r):
        for y in range(c):
            if dirties[x][y] <= 0:
                continue

            dirt = dirties[x][y] // 5
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= r or ny >= c or dirties[nx][ny] == -1:
                    continue
                ret[nx][ny] += dirt
                ret[x][y] -= dirt
    return ret


def purifyAir():
    u, d = purifier
    up_tmp = []
    for j in range(1, c):
        up_tmp.append(dirties[u][j])

    for i in range(u - 1, 0, -1):
        up_tmp.append(dirties[i][c - 1])

    for j in range(c - 1, 0, -1):
        up_tmp.append(dirties[0][j])

    for i in range(u):
        up_tmp.append(dirties[i][0])

    up_tmp.insert(0, up_tmp.pop())
    cnt = 0

    for j in range(1, c):
        dirties[u][j] = up_tmp[cnt]
        cnt += 1
    for i in range(u - 1, 0, -1):
        dirties[i][c - 1] = up_tmp[cnt]
        cnt += 1
    for j in range(c - 1, 0, -1):
        dirties[0][j] = up_tmp[cnt]
        cnt += 1
    for i in range(u):
        dirties[i][0] = up_tmp[cnt]
        cnt += 1
    dirties[u][1] = 0

    down_tmp = []
    for j in range(1, c - 1):
        down_tmp.append(dirties[d][j])

    for i in range(d, r - 1):
        down_tmp.append(dirties[i][c - 1])

    for j in range(c - 1, 0, -1):
        down_tmp.append(dirties[r - 1][j])

    for i in range(r - 1, d, -1):
        down_tmp.append(dirties[i][0])
    cnt = 0
    down_tmp.insert(0, down_tmp.pop())
    for j in range(1, c - 1):
        dirties[d][j] = down_tmp[cnt]
        cnt += 1
    for i in range(d, r - 1):
        dirties[i][c - 1] = down_tmp[cnt]
        cnt += 1
    for j in range(c - 1, 0, -1):
        dirties[r - 1][j] = down_tmp[cnt]
        cnt += 1
    for i in range(r - 1, d, -1):
        dirties[i][0] = down_tmp[cnt]
        cnt += 1
    dirties[d][1] = 0


for _ in range(t):
    dirties = spreadDirt()
    purifyAir()

print(sum(map(lambda x: sum(x), dirties)) + 2)
