# https://www.acmicpc.net/problem/3108
import sys

read = sys.stdin.readline
n = int(read().strip())
trees = [[i, 0] for i in range(n + 1)]
squares = [(0, 0, 0, 0)]

for i in range(1, n + 1):
    a, b, c, d = map(int, read().strip().split())
    a, c = min(a, c), max(a, c)
    b, d = min(b, d), max(b, d)
    squares.append((a, b, c, d))


def find(idx):
    if idx == trees[idx][0]:
        return idx
    trees[idx][0] = find(trees[idx][0])
    return trees[idx][0]


def merge(p, q):
    if trees[p][1] > trees[q][1]:
        trees[q][0] = p
    elif trees[p][1] < trees[q][1]:
        trees[p][0] = q
    else:
        trees[q][0] = p
        trees[p][1] += 1


def canOneStroke(a, b):
    if a[0] < b[0] and b[2] < a[2] and a[1] < b[1] and b[3] < a[3]:
        return False
    if a[0] > b[0] and b[2] > a[2] and a[1] > b[1] and b[3] > a[3]:
        return False
    if b[0] > a[2] or b[2] < a[0] or b[1] > a[3] or b[3] < a[1]:
        return False
    return True


for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            continue

        if canOneStroke(squares[i], squares[j]):
            p, q = find(i), find(j)
            if p != q:
                merge(p, q)

ans = set()
for i in range(n + 1):
    ans.add(find(i))
print(len(ans) - 1)
