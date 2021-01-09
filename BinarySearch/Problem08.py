# https://www.acmicpc.net/problem/2585
import sys
from collections import deque, defaultdict
from math import ceil, sqrt

read = sys.stdin.readline
n, k = map(int, read().strip().split())
stations = [tuple(map(int, read().strip().split())) for _ in range(n)]
stations.insert(0, (0, 0))
stations.append((10000, 10000))
edges = defaultdict(list)


def getDistance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


l, r = float('inf'), 0

for i in range(n):
    for j in range(i + 1, len(stations)):
        distance = getDistance(stations[i], stations[j])
        l, r = min(l, distance), max(r, distance)
        edges[i].append((j, distance))
        edges[j].append((i, distance))


def go(target):
    q = deque()
    q.append((0, 0))
    visit = [True] * (len(stations))
    visit[0] = False

    while q:
        cur, d = q.popleft()
        for nxt, w in edges[cur]:
            if visit[nxt] and w < target and d <= k:
                q.append((nxt, d + 1))
                visit[nxt] = False
    return visit[len(stations) - 1]


l, r = int(l), int(r)
while l < r:
    mid = (l + r) // 2
    if go(mid):
        l = mid + 1
    else:
        r = mid

print(ceil(r / 10))
