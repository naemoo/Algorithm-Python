# https://www.acmicpc.net/problem/14500
import sys
from copy import deepcopy

read = sys.stdin.readline
n, m = map(int, read().strip().split())
blocks = [[[1, 1], [1, 1]], [[1, 1, 1, 1]], [[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]],
          [[0, 1], [0, 1], [1, 1]], [[1, 0], [1, 0], [1, 1]], [[1, 0], [1, 1], [1, 0]]]
scores = [list(map(int, read().strip().split())) for _ in range(n)]


def roateArr(arr):
    tmp = deepcopy(arr)
    tmp.reverse()
    return list(map(list, zip(*tmp)))


for i in range(len(blocks)):
    if i == 1:
        blocks.append(roateArr(blocks[i]))
    elif 1 < i <= 3:
        tmp = blocks[i]
        for _ in range(1):
            tmp = roateArr(tmp)
            blocks.append(tmp)
    elif 3 < i:
        tmp = blocks[i]
        for _ in range(3):
            tmp = roateArr(tmp)
            blocks.append(tmp)

ans = 0


def getTotal(x, y, r, c, block):
    ret = 0
    for i in range(r):
        for j in range(c):
            nx, ny = x + i, y + j
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return -1
            ret += scores[nx][ny] if block[i][j] else 0
    return ret


for block in blocks:
    r, c = len(block), len(block[0])
    for i in range(n):
        for j in range(m):
            ans = max(ans, getTotal(i, j, r, c, block))

print(ans)
