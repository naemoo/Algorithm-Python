# https://www.acmicpc.net/problem/14428
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = list(map(int, read().strip().split()))
arr.insert(0, 0)
m = int(read().strip())
tree = [[0, 0] for _ in range(4 * n)]


def init(low, high, start, end, node=1):
    if high < start or low > end:
        return float('inf')
    if start == end:
        tree[node] = [arr[start], start]
        return tree[node]

    mid = (start + end) // 2

    right, r_idx = init(low, high, mid + 1, end, node * 2 + 1)
    left, l_idx = init(low, high, start, mid, node * 2)
    if left <= right:
        tree[node] = [left, l_idx]
    else:
        tree[node] = [right, r_idx]
    return tree[node]


def getMin(low, high, start, end, node=1):
    if start > high or end < low:
        return float('inf'), 0

    if low <= start and end <= high:
        return tree[node]

    mid = (start + end) // 2
    left = getMin(low, high, start, mid, node * 2)
    right = getMin(low, high, mid + 1, end, node * 2 + 1)
    if left[0] <= right[0]:
        return left
    else:
        return right


def update(start, end, idx, val, node=1):
    if idx < start or idx > end:
        return tree[node]

    if start == end:
        tree[node] = [val, idx]
        arr[start] = val
        return tree[node]

    mid = (start + end) // 2
    left = update(start, mid, idx, val, node * 2)
    right = update(mid + 1, end, idx, val, node * 2 + 1)
    if left[0] <= right[0]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]


init(1, n, 1, n)
while m:
    a, b, c = map(int, read().strip().split())
    if a - 1:
        print(getMin(b, c, 1, n)[1])
    else:
        update(1, n, b, c)
    m -= 1
