# https://www.acmicpc.net/problem/2610
import sys

read = sys.stdin.readline
n, m = int(read().strip()), int(read().strip())
dp = [[float('inf') if j != i else 0 for j in range(n + 1)] for i in range(n + 1)]
tree = [i for i in range(n + 1)]

while m:
    a, b = map(int, read().strip().split())
    dp[a][b] = 1
    dp[b][a] = 1
    m -= 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def find(idx):
    if tree[idx] == idx:
        return idx
    tree[idx] = find(tree[idx])
    return tree[idx]


def merge(p, q):
    p_r, q_r = 0, 0
    for i in range(1, n + 1):
        if dp[p][i] != float('inf'):
            p_r = max(p_r, dp[p][i])
        if dp[q][i] != float('inf'):
            q_r = max(q_r, dp[q][i])
    if p_r < q_r:
        tree[q] = p
    else:
        tree[p] = q


for i in range(1, n + 1):
    for j in range(1, n + 1):
        p, q = find(i), find(j)
        if p != q and dp[i][j] != float('inf'):
            merge(p, q)

committee = set(tree[1:])
print(len(committee))
for i in sorted(committee):
    print(i)
