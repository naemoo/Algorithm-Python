# https://www.acmicpc.net/problem/16724
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
rooms = [list(read().strip()) for _ in range(n)]
tree = [[i, 0] for i in range(n * m)]
directions = dict(zip(('D', 'R', 'U', 'L'), ((1, 0), (0, 1), (-1, 0), (0, -1))))


def find(idx):
    if tree[idx][0] == idx:
        return idx

    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    p, q = find(p), find(q)

    if tree[p][1] < tree[q][1]:
        tree[p][0] = q
    elif tree[p][1] > tree[q][1]:
        tree[q][0] = p
    else:
        tree[q][1] += 1
        tree[p][0] = q


def two_to_one(i, j):
    return i * m + j


ans = n * m
for x, room in enumerate(rooms):
    for y, e in enumerate(room):
        dx, dy = directions[e]
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        p, q = two_to_one(x, y), two_to_one(nx, ny)
        p, q = find(p), find(q)
        if p != q:
            merge(p, q)
            ans -= 1

print(ans)
