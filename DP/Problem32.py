import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n, k = map(int, read().strip().split())
max_len = 2 * 100000
sys.setrecursionlimit(max_len + 1)
visit = [float('inf') for _ in range(max_len + 1)]
q = []
q.append((0, n))
visit[n] = 0
while q:
    cost, cur = heappop(q)

    if visit[cur] < cost:
        continue

    for i in range(3):
        nxtCost = cost
        if i == 0:
            nxtCost += 1
            nxt = cur + 1
        elif i == 1:
            nxtCost += 1
            nxt = cur - 1
        elif i == 2:
            nxt = cur * 2

        if nxt < 0 or nxt > max_len:
            continue
        if nxtCost < visit[nxt]:
            heappush(q, (nxtCost, nxt))
            visit[nxt] = nxtCost
print(visit[k])
