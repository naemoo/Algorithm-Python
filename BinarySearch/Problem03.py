# https://www.acmicpc.net/problem/2473
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [int(e) for e in read().strip().split()]
arr.sort()
ans, ret = float('inf'), None

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        l, r = j + 1, len(arr) - 1
        pivot = arr[i] + arr[j]
        while l <= r:
            mid = (l + r) // 2
            tmp = pivot + arr[mid]
            if abs(tmp) < abs(ans):
                ans = tmp
                ret = arr[i], arr[j], arr[mid]

            if tmp > 0:
                r = mid - 1
            else:
                l = mid + 1
for e in ret:
    print(e, end=' ')
