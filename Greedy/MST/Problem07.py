# https://www.acmicpc.net/problem/6497
import sys

read = sys.stdin.readline


def find(idx):
    if tree[idx][0] != idx:
        tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    p, q = find(p), find(q)
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
    elif tree[p][1] < tree[q][1]:
        tree[p][0] = q
    else:
        tree[p][0] = q
        tree[q][1] += 1


while (tmp := tuple(map(int, read().strip().split()))) != (0, 0):
    n, m = tmp
    tree = [[i, 0] for i in range(n)]
    edges = []
    total = 0
    while m:
        x, y, z = map(int, read().strip().split())
        edges.append((z, x, y))
        total += z
        m -= 1
    edges.sort()
    ans = 0
    for z, x, y in edges:
        if find(x) != find(y):
            ans += z
            merge(x, y)
    print(total - ans)