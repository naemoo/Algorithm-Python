# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappop, heapify, heappush

read = sys.stdin.readline
n = int(read().strip())
cards = [int(read().strip()) for _ in range(n)]
heapify(cards)
ans = 0
while len(cards) != 1:
    tmp = heappop(cards)
    tmp += heappop(cards)
    heappush(cards, tmp)
    ans += tmp

print(ans)
