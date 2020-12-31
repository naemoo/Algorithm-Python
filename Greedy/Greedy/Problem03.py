# https://www.acmicpc.net/problem/2437
import sys

read = sys.stdin.readline
n = int(read())
arr = sorted(map(int, read().strip().split()))
tmp = 1

for i,e in enumerate(arr):
    if tmp < arr[i]:
        break
    tmp += e
print(tmp if arr[0] == 1 else 1)
