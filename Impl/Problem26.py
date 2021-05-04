# https://www.acmicpc.net/problem/19236
import sys
from copy import deepcopy

read = sys.stdin.readline
directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
fish = []
fish_loc = dict()
for i in range(4):
    tmp = list(map(int, read().strip().split()))
    fish.append(list(map(list, zip(tmp[0::2], map(lambda x: x - 1, tmp[1::2])))))
    for j, e in enumerate(fish[i]):
        fish_loc[e[0]] = [i, j]


def moveFish(shark, pool, fish_loc):
    for num in range(1, 17):
        if not num in fish_loc.keys():
            continue

        x, y = fish_loc[num]
        d = pool[x][y][1]
        dx, dy = directions[d]
        nx, ny = x + dx, dy + y
        cnt = 0
        while (nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or (nx, ny) == shark) and cnt < 8:
            d = (d + 1) % 8
            dx, dy = directions[d]
            nx, ny = x + dx, dy + y
            cnt += 1

        if cnt == 8:
            continue

        if cnt:
            pool[x][y][1] = d

        if pool[nx][ny]:
            pool[x][y], pool[nx][ny] = pool[nx][ny], pool[x][y]
            fish_loc[pool[x][y][0]], fish_loc[pool[nx][ny][0]] = fish_loc[pool[nx][ny][0]], fish_loc[pool[x][y][0]]
        else:
            fish_loc[pool[x][y][0]] = [nx, ny]
            pool[x][y], pool[nx][ny] = pool[nx][ny], pool[x][y]


def go(shark, d, fish, fish_loc):
    x, y = shark
    pool = deepcopy(fish)
    pool[x][y] = 0
    new_fish_loc = deepcopy(fish_loc)
    del new_fish_loc[fish[x][y][0]]
    moveFish(shark, pool, new_fish_loc)

    ret = 0
    for i in range(1, 4):
        dx, dy = directions[d]
        nx, ny = x + dx * i, y + dy * i
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or not pool[nx][ny]:
            continue

        nd = pool[nx][ny][1]
        ret = max(go((nx, ny), nd, pool, new_fish_loc), ret)

    return ret + fish[x][y][0]


print(go((0, 0), fish[0][0][1], fish, fish_loc))
