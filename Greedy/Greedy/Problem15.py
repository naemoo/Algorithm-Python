# https://www.acmicpc.net/problem/1744
import sys
from bisect import bisect_left
from collections import deque

read = sys.stdin.readline
n = int(read().strip())
arr = [int(read().strip()) for _ in range(n)]
arr.sort()
idx = bisect_left(arr, 1)
negative, positive = deque(arr[:idx]), deque(arr[idx:])
ans = 0
while negative:
    tmp = negative.popleft()
    if negative:
        tmp *= negative.popleft()
    ans += tmp

while positive:
    tmp = positive.pop()
    if positive:
        if positive[-1] != 0 and positive[-1] != 1:
            tmp *= positive.pop()
    ans += tmp

print(ans)