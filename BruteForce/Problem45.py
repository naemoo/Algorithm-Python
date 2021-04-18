# https://www.acmicpc.net/problem/1035
import sys
from collections import deque
from itertools import product, combinations, permutations

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
pieces = [list(read().strip()) for _ in range(5)]
start = []
r = 0
getDistance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

for i, piece in enumerate(pieces):
    for j, e in enumerate(piece):
        if e == '*':
            start.append((i, j))
            r += 1


def isAllConnect(combination):
    destinations = [[False for _ in range(5)] for _ in range(5)]
    visit = [[False for _ in range(5)] for _ in range(5)]

    for x, y in combination:
        destinations[x][y] = True

    q = deque([combination[0]])
    visit[combination[0][0]][combination[0][1]] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue

            if not visit[nx][ny] and destinations[nx][ny]:
                cnt += 1
                visit[nx][ny] = True
                q.append((nx, ny))

    return True if cnt == r else False


ans = float('inf')
for combination in combinations(list(product(range(5), repeat=2)), r):
    if isAllConnect(combination):
        for permutation in permutations(combination, r):
            tmp = 0
            for a, b in zip(permutation, start):
                tmp += getDistance(a, b)
            ans = min(ans, tmp)

print(ans)
