# https://www.acmicpc.net/problem/1655
from heapq import heappush, heappop
import sys

read = sys.stdin.readline
n = int(read().strip())

minh = []
maxh = []

while n:
    num = int(read().strip())

    if len(maxh) > len(minh):
        heappush(minh, num)
    else:
        heappush(maxh, -num)

    if minh and maxh and -maxh[0] > minh[0]:
        minTop, maxTop = heappop(minh), -heappop(maxh)
        heappush(maxh, -minTop)
        heappush(minh, maxTop)

    print(-maxh[0])
    n -= 1
