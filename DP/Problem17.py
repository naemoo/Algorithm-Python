# https://www.acmicpc.net/problem/11659
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
prefix = []

tmp = 0
for e in arr:
    prefix.append(tmp)
    tmp += e
prefix.append(tmp)

while m:
    i, j = map(int, read().strip().split())
    print(prefix[j] - prefix[i - 1])
    m -= 1
