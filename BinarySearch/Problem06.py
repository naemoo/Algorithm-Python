# https://www.acmicpc.net/problem/18870
import sys

read = sys.stdin.readline
n = int(read())
x = [int(e) for e in read().strip().split()]


def lower(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


nx = sorted(set(x))
for i, e in enumerate(x):
    x[i] = lower(nx, e)
for e in x:
    print(e, end=' ')
