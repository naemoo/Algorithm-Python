# https://www.acmicpc.net/problem/13334
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
n = int(read().strip())
tracks = []
for _ in range(n):
    h, o = map(int, read().strip().split())
    tracks.append((min(h, o), max(h, o)))
d = int(read().strip())
tracks.sort(key=lambda x: x[1])
q = []
ans = 0
for track in tracks:
    heappush(q, track)
    while q and q[0][0] < track[1] - d:
        heappop(q)
    ans = max(len(q), ans)
print(ans)