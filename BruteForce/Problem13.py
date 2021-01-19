# https://www.acmicpc.net/problem/2580
import sys

read = sys.stdin.readline
games = [list(map(int, read().strip().split())) for _ in range(9)]
blanks = []

for i, game in enumerate(games):
    for j, e in enumerate(game):
        if e == 0:
            blanks.append((i, j))


def canPut(x, y, e):
    startX, startY = (x // 3) * 3, (y // 3) * 3
    for i in range(startX, startX + 3):
        for j in range(startY, startY + 3):
            tmp = games[i][j]
            if tmp == 0:
                continue
            if tmp == e:
                return False

    for i in range(9):
        tmp = games[x][i]
        if tmp == 0:
            continue
        if tmp == e:
            return False

    for i in range(9):
        tmp = games[i][y]
        if tmp == 0:
            continue
        if tmp == e:
            return False
    return True


def startGame(d):
    if d == len(blanks):
        for game in games:
            for e in game:
                print(e, end=' ')
            print()
        exit()

    x, y = blanks[d]
    for i in range(1, 10):
        if canPut(x, y, i):
            games[x][y] = i
            startGame(d + 1)
            games[x][y] = 0

startGame(0)
