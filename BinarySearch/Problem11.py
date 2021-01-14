# https://www.acmicpc.net/problem/1365
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [int(e) for e in read().strip().split()]
lis = []


def lower(arr, target):
    l, r = 0, len(arr),

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


for e in arr:
    idx = lower(lis, e)
    if idx == len(lis):
        lis.append(e)
    else:
        lis[idx] = e

print(n - len(lis))
