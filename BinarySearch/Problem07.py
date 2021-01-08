# https://www.acmicpc.net/problem/1477
import sys

read = sys.stdin.readline
n, m, l = map(int, read().strip().split())
arr = [int(e) for e in read().strip().split()]
arr.insert(0, 0)
arr.append(l)
arr.sort()

start, end = 1, l - 1


def canGo(target):
    tmp = 0
    for i in range(len(arr) - 1):
        tmp += (arr[i + 1] - arr[i] - 1) // target
    return True if tmp > m else False


while start < end:
    mid = (start + end) // 2

    if canGo(mid):
        start = mid + 1
    else:
        end = mid
print(end)
