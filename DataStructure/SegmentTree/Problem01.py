# https://www.acmicpc.net/problem/7578
import sys

read = sys.stdin.readline
n = int(read())
A = list(map(int, read().strip().split()))
B = list(map(int, read().strip().split()))
bInfos = {}
for i, b in enumerate(B):
    bInfos[b] = i + 1

tree = [0] * (n + 1)


def update(idx, num):
    while idx > 0:
        tree[idx] += num
        idx -= (idx & -idx)


def sum(idx):
    ret = 0
    while idx < len(tree):
        ret += tree[idx]
        idx += (idx & -idx)
    return ret


ans = 0
for a in A:
    ans += sum(bInfos[a])
    update(bInfos[a], 1)
print(ans)