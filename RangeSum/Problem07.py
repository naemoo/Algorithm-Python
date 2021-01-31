# https://www.acmicpc.net/problem/2003
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))

total = 0
end = 0
ans = 0

for start in range(n):

    while total < m and end < n:
        total += arr[end]
        end += 1
    if total == m:
        ans += 1
    total -= arr[start]

print(ans)
