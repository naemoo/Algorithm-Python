# https://www.acmicpc.net/problem/14476
import sys
from math import gcd

read = sys.stdin.readline
n = int(read().strip())
arr = [int(e) for e in read().strip().split()]
arr.sort()

left = [arr[0]]
right = [arr[-1]]

for i in range(1, n):
    left.append(gcd(left[-1], arr[i]))

for i in range(n - 1, -1, -1):
    right.append(gcd(right[-1], arr[i]))

right.reverse()
ret = -1
idx = -1
for i in range(n):
    if i != 0 and i != n - 1:
        tmp = gcd(left[i - 1], right[i + 1])
    elif i == 0:
        tmp = right[1]
    else:
        tmp = left[n - 2]
    if ret < tmp:
        ret = tmp
        idx = i

if gcd(arr[idx], ret) == ret:
    print(-1)
else:
    print(ret, arr[idx])
