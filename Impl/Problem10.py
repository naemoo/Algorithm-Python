# https://www.acmicpc.net/problem/16234
import sys

read = sys.stdin.readline
n, l, r = map(int, read().strip().split())
country = [list(map(int, read().strip().split())) for _ in range(n)]
ans = 0

def find(idx):
    if tree[idx][0] == idx:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
        tree[p][1] += tree[q][1]
        tree[p][2] += tree[q][2]
    elif tree[p][1] < tree[q][1]:
        tree[p][0] = q
        tree[q][1] += tree[p][1]
        tree[q][2] += tree[p][2]
    else:
        tree[p][0] = q
        tree[q][1] += tree[p][1]
        tree[q][2] += tree[p][2]


while True:
    cnt = 0
    tree = [[i, 1, country[i // n][i % n]] for i in range(n * n)]
    for i in range(n):
        for j in range(n):
            if i + 1 < n and l <= abs(country[i][j] - country[i + 1][j]) <= r:
                p, q = find(i * n + j), find((i + 1) * n + j)
                if p != q:
                    merge(p, q)
                    cnt += 1
            if j + 1 < n and l <= abs(country[i][j] - country[i][j + 1]) <= r:
                p, q = find(i * n + j), find(i * n + j + 1)
                if p != q:
                    merge(p, q)
                    cnt += 1

    if not cnt:
        break

    for i in range(n):
        for j in range(n):
            head = find(i * n + j)
            country[i][j] = tree[head][2] // tree[head][1]
    
    ans += 1
print(ans)
