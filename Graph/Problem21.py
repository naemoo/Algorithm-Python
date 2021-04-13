# https://www.acmicpc.net/problem/17090
import sys
from collections import Counter

read = sys.stdin.readline
n, m = map(int, read().strip().split())
mazes = [read().strip() for _ in range(n)]
directions = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}
exits = []
tree = [[i, 1] for i in range(n * m)]


def find(idx):
    if tree[idx][0] == idx:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
        tree[p][1] += tree[q][1]
    else:
        tree[p][0] = q
        tree[q][1] += tree[p][1]


for x, maze in enumerate(mazes):
    for y, e in enumerate(maze):
        dx, dy = directions[e]
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            exits.append((x, y))
        else:
            p, q = find(x * m + y), find(nx * m + ny)
            if p != q:
                merge(p, q)

cnt = Counter(map(lambda x: find(x), range(n * m)))
ans = 0
for x, y in exits:
    ans += cnt[find(x * m + y)]
print(ans)
