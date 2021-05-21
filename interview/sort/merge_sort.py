# https://www.acmicpc.net/problem/2751
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [int(read().strip()) for _ in range(n)]
ret = [0] * n


def merge_sort(arr, l, r):
    if l >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    p, q = l, mid + 1
    idx = l
    # merge
    while p <= mid and q <= r:
        if arr[p] >= arr[q]:
            ret[idx] = arr[q]
            q += 1
        else:
            ret[idx] = arr[p]
            p += 1
        idx += 1

    if p <= mid:
        for e in arr[p:mid + 1]:
            ret[idx] = e
            idx += 1
    if q <= r:
        for e in arr[q:r + 1]:
            ret[idx] = e
            idx += 1

    arr[l:r + 1] = ret[l:r + 1]


merge_sort(arr, 0, n - 1)
print(*arr, sep='\n')
