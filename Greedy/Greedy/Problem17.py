# https://www.acmicpc.net/problem/1461
import sys
from bisect import bisect_left

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
arr.sort()
start = bisect_left(arr, 0)
p_arr = arr[start:]
p_arr.reverse()
n_arr = arr[:start]
max_value = 0
for p in p_arr:
    max_value = max(max_value, p)
for n in n_arr:
    max_value = max(max_value, abs(n))

lst = []
for i in range(0, len(p_arr), m):
    if max_value != p_arr[i]:
        lst.append(p_arr[i])

for i in range(0, len(n_arr), m):
    if max_value != abs(n_arr[i]):
        lst.append(n_arr[i])

ans = max_value
for e in lst:
    ans += abs(e * 2)
print(ans)
