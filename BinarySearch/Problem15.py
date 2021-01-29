# https://www.acmicpc.net/problem/2143
import sys

read = sys.stdin.readline
t = int(read().strip())

n = int(read().strip())
A = list(map(int, read().strip().split()))
m = int(read().strip())
B = list(map(int, read().strip().split()))

end = 0
sA = list()
sB = list()
for i in range(len(A)):
    total = 0
    for j in range(i, n):
        total += A[j]
        sA.append(total)

for i in range(len(B)):
    total = 0
    for j in range(i, m):
        total += B[j]
        sB.append(total)

sA.sort()
sB.sort()


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


ret = 0
for e in sA:
    a, b = lower(sB, t - e), upper(sB, t - e)
    ret += b - a
print(ret)