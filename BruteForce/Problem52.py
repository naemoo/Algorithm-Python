# https://www.acmicpc.net/problem/14939
import sys
from copy import deepcopy

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
lights = [[1 if i == 'O' else 0 for i in read().strip()] for _ in range(10)]
ans = float('inf')


def isDown(tmp):
    for row in tmp:
        for e in row:
            if e:
                return False
    return True


for state in range(1 << 10):
    tmp = deepcopy(lights)
    cnt = 0

    for i in range(10):
        if state & (1 << i):
            cnt += 1
            tmp[0][i] = 1 - tmp[0][i]
            for dx, dy in directions:
                nx, ny = 0 + dx, i + dy
                if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                    continue
                tmp[nx][ny] = 1 - tmp[nx][ny]

    for x in range(1, 10):
        for y in range(10):
            if tmp[x - 1][y]:
                cnt += 1
                tmp[x][y] = 1 - tmp[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                        continue
                    tmp[nx][ny] = 1 - tmp[nx][ny]

    if isDown(tmp):
        ans = min(ans, cnt)

print(ans)
