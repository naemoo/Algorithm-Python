# # https://www.acmicpc.net/problem/2268
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = [0 for _ in range(n + 1)]
tree = [0 for _ in range(4 * n)]


def getSum(low, high, start, end, node=1):
    if end < low or start > high:
        return 0

    if low <= start and end <= high:
        return tree[node]

    mid = (start + end) // 2
    return getSum(low, high, start, mid, node * 2) + getSum(low, high, mid + 1, end, node * 2 + 1)


def update(low, high, idx, val, node=1):
    if idx < low or idx > high:
        return
    tree[node] += val
    if low == high:
        return
    mid = (low + high) // 2
    update(low, mid, idx, val, node * 2)
    update(mid + 1, high, idx, val, node * 2 + 1)


for _ in range(m):
    a, b, c = map(int, read().strip().split())
    if a:
        update(1, n, b, -arr[b] + c)
        arr[b] = c
    else:
        b, c = min(b, c), max(b, c)
        print(getSum(b, c, 1, n))
