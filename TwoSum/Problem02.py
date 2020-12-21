# https://www.acmicpc.net/problem/2473
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [e for e in map(int, read().strip().split())]
arr.sort()
ans, ret = float('inf'), None

for i in range(len(arr)):
    l, r = i + 1, len(arr) - 1

    while l < r:
        tmp = arr[i] + arr[l] + arr[r]

        if abs(tmp) < abs(ans):
            ans = tmp
            ret = arr[i], arr[l], arr[r]
        if tmp > 0:
            r -= 1
        else:
            l += 1
for e in ret:
    print(e,end=' ')
