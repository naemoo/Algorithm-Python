# https://www.acmicpc.net/problem/1208
import sys
from collections import Counter

read = sys.stdin.readline
n, s = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
mid = n // 2
arr1 = arr[:mid]
arr2 = arr[n // 2:]
sub1 = []
sub2 = []
for i in range(1 << len(arr1)):
    tmp = 0
    for j in range(len(arr1)):
        if i & 1:
            tmp += arr1[j]
        i = i >> 1
    sub1.append(tmp)
for i in range(1 << len(arr2)):
    tmp = 0
    for j in range(len(arr2)):
        if i & 1:
            tmp += arr2[j]
        i = i >> 1
    sub2.append(tmp)
sub1 = Counter(sub1)
ans = 0
for e in sub2:
    t = s - e
    if t in sub1.keys():
        ans += sub1[t]
if s == 0:
    ans -= 1
print(ans)
