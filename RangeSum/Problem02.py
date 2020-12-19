# https://www.acmicpc.net/problem/1806
import sys

inp = sys.stdin.readline
n, s = map(int, inp().strip().split())
arr = list(map(int, inp().strip().split()))

end, ans, total = 0, float('inf'), 0

for start in range(len(arr)):

    while total < s and end < len(arr):
        total += arr[end]
        end += 1

    if total >= s:
        ans = min(ans, end - start)

    total -= arr[start]

print(ans if ans != float('inf') else 0)