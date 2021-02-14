# https://www.acmicpc.net/problem/10423
import sys

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
trees = [[i, 0] for i in range(n + 1)]
plants = list(map(int, read().strip().split()))
edges = [tuple(map(int, read().strip().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])


def find(idx):
    if trees[idx][0] == idx:
        return idx
    trees[idx][0] = find(trees[idx][0])
    return trees[idx][0]


def merge(a, b):
    a, b = find(a), find(b)

    if trees[a][1] < trees[b][1]:
        trees[a][0] = b
    elif trees[a][1] > trees[b][1]:
        trees[b][0] = a
    else:
        trees[a][0] = b
        trees[b][1] += 1


for i in range(1, len(plants)):
    merge(plants[i], plants[i - 1])

ans = 0
for a, b, w in edges:
    a, b = find(a), find(b)
    if a != b:
        merge(a, b)
        ans += w
print(ans)
