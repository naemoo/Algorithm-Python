# https://www.acmicpc.net/problem/8983
import sys

read = sys.stdin.readline
m, n, l = map(int, read().strip().split())
loc = list(map(int, read().strip().split()))
animals = []

for _ in range(n):
    animals.append(tuple(map(int, read().strip().split())))

loc.sort()


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
    l, r = 0, len(arr),
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return r


ret = 0
for a, b in animals:
    m1 = a + b - l
    m2 = l - b + a
    a = lower(loc, m1)
    b = upper(loc, m2) - 1
    ret += 1 if (b - a + 1) > 0 else 0
print(ret)
