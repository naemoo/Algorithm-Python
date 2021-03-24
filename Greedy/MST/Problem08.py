# https://www.acmicpc.net/problem/14621
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
gender = read().strip().split()
gender.insert(0, None)
edges = []
while m:
    a, b, w = map(int, read().strip().split())
    if gender[a] != gender[b]:
        edges.append((w, a, b))
    m -= 1

tree = [[i, 0] for i in range(n + 1)]
edges.sort()


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


ans = 0
cnt = 0
for w, a, b in edges:
    a, b = find(a), find(b)
    if a != b:
        merge(a, b)
        ans += w
        cnt += 1

print(ans if cnt == n - 1 else -1)
