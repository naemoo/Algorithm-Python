# https://www.acmicpc.net/problem/3020
import sys

inp = sys.stdin.readline
n, h = map(int, inp().strip().split())

floors = []
ceiling = []

for i in range(n):
    obstacle = int(inp().strip())
    if i % 2 == 0:
        floors.append(obstacle)
    else:
        ceiling.append(obstacle)
floors.sort(), ceiling.sort()


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


ans, cnt = float('inf'), 0
print(floors)
print(ceiling)

for i in range(1, h + 1):
    tmp = len(floors) - lower(floors, i) + len(ceiling) - upper(ceiling, h - i)
    if tmp < ans:
        cnt = 1
        ans = tmp
    elif tmp == ans:
        cnt += 1

print(ans, cnt)
