# https://www.acmicpc.net/problem/15678
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n, d = map(int, read().strip().split())
bridges = list(map(int, read().strip().split()))
dp = [0 for _ in range(n)]
q = []

for i, bridge in enumerate(bridges):
    while q and q[0][1] < i - d:
        heappop(q)
    if q:
        dp[i] = max(bridge - q[0][0], bridge)
    else:
        dp[i] = bridge
    heappush(q, (-dp[i], i))

print(max(dp))
