# https://www.acmicpc.net/problem/12100
import sys
from copy import deepcopy
from itertools import product
from collections import deque

read = sys.stdin.readline
n = int(read().strip())
arr = [list(map(int, read().strip().split())) for _ in range(n)]


def playGame(game, dir):
    if dir == 0:
        for rn, row in enumerate(game):
            row = deque(filter(lambda x: x != 0, row))
            cnt = n - len(row)
            for i in range(len(row) - 1, 0, -1):
                if row[i] and row[i] == row[i - 1]:
                    row[i] *= 2
                    row[i - 1] = 0
                    for j in range(i - 1, 0, -1):
                        row[j], row[j - 1] = row[j - 1], row[j]
            game[rn] = row
            while cnt:
                row.appendleft(0)
                cnt -= 1
    elif dir == 1:
        for rn, row in enumerate(game):
            row = list(filter(lambda x: x != 0, row))
            cnt = n - len(row)
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    row[i + 1] = 0
                    for j in range(i + 1, len(row) - 1):
                        row[j], row[j + 1] = row[j + 1], row[j]
            game[rn] = row
            while cnt:
                row.append(0)
                cnt -= 1
    else:
        game = list(map(list, zip(*game)))
        game = list(map(list, zip(*playGame(game, dir % 2))))
    return game


ans = 0
for e in product(range(4), repeat=5):
    game = deepcopy(arr)
    for i in e:
        game = playGame(game, i)
    ans = max(max(map(max, game)), ans)
print(ans)
