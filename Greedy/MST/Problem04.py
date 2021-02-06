# https://www.acmicpc.net/problem/1647
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())

tree = [[i, 0] for i in range(n + 1)]


def find(idx):
    if idx == tree[idx][0]:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    p, q = find(p), find(q)
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
    elif tree[p][1] < tree[q][1]:
        tree[p][0] = q
    else:
        tree[q][0] = p
        tree[p][1] += 1


paths = []

while m:
    a, b, c = map(int, read().strip().split())
    paths.append((c, a, b))
    m -= 1

paths.sort()

cnt = 0
ret = 0
for c, a, b in paths:
    a, b = find(a), find(b)
    if a != b:
        merge(a, b)
        cnt += 1
        ret += c
    if cnt == n - 2:
        break
print(ret)
