# https://www.acmicpc.net/problem/17406
import sys
from itertools import permutations
from copy import deepcopy

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, read().strip().split())) for _ in range(n)]
op = [tuple(map(int, read().strip().split())) for _ in range(k)]


def rotateArr(arr, left, right):
    lx, ly = left
    rx, ry = right
    seq = (ry - ly, rx - lx, ry - ly, rx - lx - 1)
    tmp = [arr[lx][ly]]
    x, y = left
    for i, e in enumerate(seq):
        dx, dy = directions[i]
        for _ in range(e):
            x, y = x + dx, y + dy
            tmp.append(arr[x][y])
    x, y = lx, ly
    arr[x][y] = tmp.pop()
    cnt = 0
    for i, e in enumerate(seq):
        dx, dy = directions[i]
        for _ in range(e):
            x, y = x + dx, y + dy
            arr[x][y] = tmp[cnt]
            cnt += 1


ans = float('inf')
for seq in permutations(op, k):
    cp_arr = deepcopy(arr)
    for r, c, s in seq:
        lx, ly, rx, ry = r - s - 1, c - s - 1, r + s - 1, c + s - 1
        while (lx, ly) < (rx, ry):
            rotateArr(cp_arr, (lx, ly), (rx, ry))
            lx, ly = lx + 1, ly + 1
            rx, ry = rx - 1, ry - 1

    for e in cp_arr:
        ans = min(sum(e), ans)

print(ans)
