# https://www.acmicpc.net/problem/2812
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
nums = list(map(int, read().strip()))
arr = [-1 for _ in range(n)]
s = []

for i in range(n):
    while s and s[-1][1] < nums[i]:
        idx, tmp = s.pop()
        arr[idx] = (i, nums[i])
    s.append((i, nums[i]))

ans = []
cnt = 0
i = 0

while i < len(arr) and cnt <= k:
    nxt = 1

    if arr[i] != -1 and arr[i][0] - i <= k - cnt:
        nxt = arr[i][0] - i
        cnt += (arr[i][0] - i)
    else:
        ans.append(nums[i])
    i += nxt

if cnt < k:
    del ans[cnt - k:]

print("".join(map(str, ans)))
