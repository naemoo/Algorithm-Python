# https://www.acmicpc.net/problem/12837
import sys

read = sys.stdin.readline
n, q = map(int, read().strip().split())
tree = [0 for _ in range(4 * n)]


def getSum(low, high, start, end, node=1):
    if start > high or end < low:
        return 0
    if low <= start and end <= high:
        return tree[node]

    mid = (start + end) // 2
    return getSum(low, high, start, mid, node * 2) + getSum(low, high, mid + 1, end, node * 2 + 1)


def update(start, end, idx, val, node=1):
    if idx < start or end < idx:
        return
    tree[node] += val
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx, val, node * 2)
    update(mid + 1, end, idx, val, node * 2 + 1)


while q:
    a, b, c = map(int, read().strip().split())
    if a - 1:
        print(getSum(b, c, 1, n))
    else:
        update(1, n, b, c)
    q -= 1
