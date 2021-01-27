# https://www.acmicpc.net/problem/1976
import sys

read = sys.stdin.readline
n = int(read().strip())
m = int(read().strip())
cities = [list(map(int, read().strip().split())) for _ in range(n)]
plans = list(map(int, read().strip().split()))
tree = [[i, 0] for i in range(n)]


def find(idx):
    if idx == tree[idx][0]:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    p, q = find(p), find(q)
    if p == q:
        return
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
    elif tree[q][1] > tree[p][1]:
        tree[p][0] = q
    else:
        tree[q][0] = p
        tree[q][1] += 1


for i, city in enumerate(cities):
    for j, e in enumerate(city):
        if e:
            merge(i, j)

cur = plans[0] - 1
for i in range(1, len(plans)):
    p, q = find(cur), find(plans[i] - 1)
    if p != q:
        print('NO')
        sys.exit()
    cur = plans[i] - 1
print('YES')
