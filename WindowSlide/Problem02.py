# https://www.acmicpc.net/problem/13305
import sys

read = sys.stdin.readline
n = int(read().strip())
distance = [int(e) for e in read().strip().split()]
villages = [int(e) for e in read().strip().split()]

start, end = 0, 0
ret = 0
while start < n - 1:
    while end < n - 1 and villages[start] <= villages[end]:
        ret += (distance[end] * villages[start])
        end += 1
    start = end

print(ret)
