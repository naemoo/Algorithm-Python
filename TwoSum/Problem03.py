# https://www.acmicpc.net/problem/2230
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = []
for _ in range(n):
    arr.append(int(read().strip()))

arr.sort()

end, ret = 0, float('inf')
tmp = -1

for start in range(len(arr)):
    while end < n and tmp < m:
        tmp = arr[end] - arr[start]
        if tmp >= m:
            ret = min(tmp, ret)
            break
        else:
            end += 1
    tmp = -1
print(ret)
