# https://www.acmicpc.net/problem/16235
import sys
from collections import defaultdict

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1))
n, m, k = map(int, read().strip().split())
a = [list(map(int, read().strip().split())) for _ in range(n)]
grounds = [[5 for _ in range(n)] for _ in range(n)]
trees = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, read().strip().split())
    trees[(x - 1, y - 1)].append(z)

for x, y in trees:
    trees[(x, y)].sort(reverse=True)

for _ in range(k):
    # spring
    for (x, y), tree in trees.items():
        d_idx = -1
        for i in range(len(tree) - 1, -1, -1):
            if grounds[x][y] >= tree[i]:
                grounds[x][y] -= tree[i]
                tree[i] += 1
            else:
                d_idx = i
                break

        if d_idx >= 0:
            for i in range(d_idx + 1):
                grounds[x][y] += tree[i] // 2
            del tree[:d_idx + 1]

    # fall
    new_tree = []
    for x, y in trees:
        for i, z in enumerate(trees[(x, y)]):
            if z % 5 == 0:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    new_tree.append((nx, ny))

    for x, y in new_tree:
        trees[(x, y)].append(1)

    # winter
    for i in range(n):
        for j in range(n):
            grounds[i][j] += a[i][j]

print(sum(map(len, trees.values())))
