# https://www.acmicpc.net/problem/16398
import sys

read = sys.stdin.readline
n = int(read().strip())
edges = []
tree = [[i, 0] for i in range(n + 1)]
for i in range(1, n):
    for j, e in enumerate(map(int, read().strip().split()), start=1):
        if i < j:
            edges.append((e, i, j))
ans = 0


def find(idx):
    if idx == tree[idx][0]:
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
        tree[p][0] = q
        tree[q][1] += 1


edges.sort()
cnt = 0
for w, a, b in edges:
    a, b = find(a), find(b),
    if a != b:
        merge(a, b)
        ans += w
        cnt += 1

    if cnt == n-1:
        print(ans)
        sys.exit()
