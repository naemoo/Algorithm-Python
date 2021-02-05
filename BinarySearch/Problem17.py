# https://www.acmicpc.net/problem/7453
import sys

read = sys.stdin.readline
n = int(read().strip())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, read().strip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

CD = []
for i in range(n):
    for j in range(n):
        CD.append(C[i] + D[j])


def lower(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


def upper(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return r


CD.sort()
ret = 0
for i in range(n):
    for j in range(n):
        e = A[i] + B[j]
        a, b = lower(CD, -e), upper(CD, -e)
        ret += b - a

print(ret)
