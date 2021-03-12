# https://www.acmicpc.net/problem/11505
import sys
from itertools import chain

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
arr = list(chain([0], [int(read().strip()) for _ in range(n)]))
tree = [0 for _ in range(4 * n)]


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return arr[start]

    mid = (start + end) // 2
    tree[node] = (init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)) % 1000000007
    return tree[node]


def getSum(low, high, start, end, node=1):
    if end < low or high < start:
        return 1
    if low <= start and end <= high:
        return tree[node]
    mid = (start + end) // 2
    return (getSum(low, high, start, mid, node * 2) * getSum(low, high, mid + 1, end, node * 2 + 1)) % 1000000007


def update(start, end, val, idx, node=1):
    if idx < start or end < idx:
        return tree[node]
    if start == end:
        tree[node] = val
        return val
    mid = (start + end) // 2
    tree[node] = (update(start, mid, val, idx, node * 2) * update(mid + 1, end, val, idx, node * 2 + 1)) % 1000000007
    return tree[node]


init(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, read().strip().split())
    if a - 1:
        print(getSum(b, c, 1, n))
    else:
        update(1, n, c, b)
