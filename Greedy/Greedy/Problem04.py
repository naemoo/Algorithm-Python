# https://www.acmicpc.net/problem/2217
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = []
for _ in range(n):
    arr.append(int(read().strip()))

ans = 0

for i, e in enumerate(sorted(arr, reverse=True)):
    ans = max(ans, e * (i + 1))
print(ans)