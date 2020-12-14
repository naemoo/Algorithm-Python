# https://www.acmicpc.net/problem/12015
import sys

input = sys.stdin.readline
n = int(input().strip())
arr = [e for e in map(int,input().strip().split())]

def binary(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right
ans = []
for e in arr:
    idx = binary(ans, e)
    if idx == len(ans):
        ans.append(e)
    else:
        ans[idx] = e
print(len(ans))


