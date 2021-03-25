# https://www.acmicpc.net/problem/2212
import sys
from collections import Counter

read = sys.stdin.readline
n = int(read().strip())
cranes = list(map(int, read().strip().split()))
cranes.sort()
m = int(read().strip())
boxes = list(map(int, read().strip().split()))
boxes.sort(reverse=True)
ships = Counter()


def lower(arr, e):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < e:
            l = mid + 1
        else:
            r = mid
    return r


for box in boxes:
    idx = lower(cranes, box)
    if idx == n:
        print(-1)
        sys.exit()
    tmp = [float('inf'), -1]
    for i in range(idx, n):
        if ships[i] < tmp[0]:
            tmp[0] = ships[i]
            tmp[1] = i
    ships[tmp[1]] += 1

print(max(ships.values()))
