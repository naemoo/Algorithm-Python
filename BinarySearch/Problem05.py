# https://www.acmicpc.net/problem/2230
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = []
for _ in range(n):
    arr.append(int(read().strip()))

arr.sort()
def lower(arr,target):
    l,r = 0,len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r

ret = float('inf')

for e in arr:
    i = lower(arr, e + m)

    if i != n:
        ret = min(ret,arr[i] - e)
print(ret)



