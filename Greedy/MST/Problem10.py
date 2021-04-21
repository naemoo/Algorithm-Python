# https://www.acmicpc.net/problem/1368
import sys

read = sys.stdin.readline
n = int(read().strip())
edges = [(0, i, int(read().strip())) for i in range(1, n + 1)]
for i in range(1, n + 1):
    for j, e in enumerate(map(int, read().strip().split()[i:]), start=i + 1):
        edges.append((i, j, e))

tree = [[i, 0] for i in range(n + 1)]


def find(idx):
    if idx == tree[idx][0]:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(a, b):
    if tree[a][1] > tree[b][1]:
        tree[b][0] = a
        tree[a][1] += tree[b][1]
    else:
        tree[a][0] = b
        tree[b][1] += tree[a][1]


ans = 0
edges.sort(key=lambda x: x[2])
for a, b, w in edges:
    a, b = find(a), find(b)
    if a != b:
        ans += w
        merge(a, b)
print(ans)
