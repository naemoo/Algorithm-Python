# https://www.acmicpc.net/problem/3197
import sys
from collections import deque

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c = map(int, read().strip().split())
lakes = [read().strip() for _ in range(r)]
q = deque()

tree = [[i, 0] for i in range(r * c)]


def find(idx):
    if tree[idx][0] == idx:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    if tree[p][1] < tree[q][1]:
        tree[p][0] = q
    elif tree[p][1] > tree[q][1]:
        tree[q][0] = p
    else:
        tree[p][0] = q
        tree[q][1] += 1


visit = [[False for _ in range(c)] for _ in range(r)]
swans = []
day = 0


def convert1D(x, y):
    return x * c + y


for i, lake in enumerate(lakes):
    for j, e in enumerate(lake):
        if e != 'X':
            if e == 'L':
                swans.append(convert1D(i, j))
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if ni < 0 or nj < 0 or ni >= r or nj >= c:
                    continue
                if lakes[ni][nj] != 'X':
                    na, a = find(convert1D(ni, nj)), find(convert1D(i, j))
                    if a != na:
                        merge(a, na)
            q.append((i, j, 0))
            visit[i][j] = True


def again(x, y):
    p = convert1D(x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        q = convert1D(nx, ny)
        if find(p) != find(q):
            merge(p, q)


sq = deque()


def ice_bfs():
    for i in range(len(q)):
        x, y, d = q.popleft()
        for dx, dy in directions:
            nx, ny, nd = dx + x, dy + y, d + 1

            if nx < 0 or ny < 0 or nx >= r or ny >= c or visit[nx][ny]:
                continue

            q.append((nx, ny, nd))
            visit[nx][ny] = True
            sq.append((nx, ny))


def set_bfs():
    while sq:
        x, y = sq.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if visit[nx][ny]:
                a, b = find(convert1D(x, y)), find(convert1D(nx, ny))
                if a != b:
                    merge(a, b)


while True:
    ice_bfs()
    a, b = find(swans[0]), find(swans[1])
    if a == b:
        break
    set_bfs()
    day += 1
print(day)
