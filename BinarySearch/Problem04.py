# https://www.acmicpc.net/problem/1939
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
roads = defaultdict(list)

l, r = float('inf'), 0

for _ in range(m):
    start, to, w = map(int, read().strip().split())
    l, r = min(l, w), max(r, w)
    roads[start].append((to, w))
    roads[to].append((start, w))

start, destination = map(int, read().strip().split())


def canReach(start, destination, target):
    visit = [True] * (n + 1)
    visit[start] = False
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        for nxt, w in roads[cur]:
            if visit[nxt] and target <= w:
                q.append(nxt)
                visit[nxt] = False
    return not visit[destination]


while l < r:
    mid = (l + r + 1) // 2

    if canReach(start, destination, mid):
        l = mid
    else:
        r = mid - 1

print(l)
