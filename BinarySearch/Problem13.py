# https://www.acmicpc.net/problem/14003
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [int(e) for e in read().strip().split()]


def lower(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


lis = []
parr = [-1 for _ in range(n)]
for i, e in enumerate(arr):
    idx = lower(lis, e)
    if idx == len(lis):
        lis.append(e)
    else:
        lis[idx] = e
    parr[i] = idx

print(len(lis))
ans = []
idx = len(lis) - 1
for i in range(len(parr) - 1, -1, -1):
    if parr[i] == idx:
        ans.append(arr[i])
        idx -= 1

while ans:
    print(ans.pop(), end=' ')
