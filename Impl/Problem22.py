# https://www.acmicpc.net/problem/20057
import sys
from copy import deepcopy


def rotateArr(arr):
    tmp = deepcopy(arr)
    tmp.reverse()
    return list(map(list, zip(*tmp)))


read = sys.stdin.readline
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
n = int(read().strip())
sands = [list(map(int, read().strip().split())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
winds = [[0, 0, 0.02, 0], [0, 0.10, 0.07, 0.01], [0.05, 0, 0, 0], [0, 0.10, 0.07, 0.01], [0, 0, 0.02, 0]]
winds_dir = {0: winds, 1: rotateArr(rotateArr(rotateArr(winds))), 2: rotateArr(rotateArr(winds)), 3: rotateArr(winds)}
start_dir = {0: (-2, -3), 1: (0, -2), 2: (-2, 0), 3: (-3, -2)}
total = sum(map(sum, sands))
x, y = (n // 2, n // 2)
cnt = 0
m_cnt = 1
d_idx = 0


def moveSand(dep, d):
    x, y = dep
    r, c = start_dir[d]

    tmp = winds_dir[d]
    px, py = x + r, y + c
    yx, yy = x + directions[d][0], y + directions[d][1]
    total = sands[yx][yy]
    sands[yx][yy] = 0
    asand = total

    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            nx, ny = px + i, py + j
            sand = int(tmp[i][j] * total)
            asand -= sand
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            sands[nx][ny] += sand

    ax, ay = x + directions[d][0] * 2, y + directions[d][1] * 2
    if not (ax < 0 or ay < 0 or ax >= n or ay >= n):
        sands[ax][ay] += asand


while (x, y) != (0, -1):
    for _ in range(m_cnt):
        dx, dy = directions[d_idx]
        moveSand((x, y), d_idx)
        x, y = x + dx, y + dy

    cnt += 1
    d_idx = (d_idx + 1) % 4
    if cnt % 2 == 0:
        cnt = 0
        m_cnt += 1

print(total - sum(map(sum, sands)))
