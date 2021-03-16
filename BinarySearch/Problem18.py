# https://www.acmicpc.net/problem/2568
import sys
from bisect import bisect_left

read = sys.stdin.readline
n = int(read().strip())
lines = [tuple(map(int, read().strip().split())) for _ in range(n)]
lines.sort()
lis = []
lis_idx = []
for a, b in lines:
    idx = bisect_left(lis, b)
    if idx == len(lis):
        lis.append(b)
    else:
        lis[idx] = b
    lis_idx.append((a, idx))

print(n - len(lis))
idx = len(lis) - 1
ans = []
for i in range(len(lis_idx) - 1, -1, -1):
    if idx != lis_idx[i][1]:
        ans.append(lis_idx[i][0])
    else:
        idx -= 1
while ans:
    print(ans.pop())
