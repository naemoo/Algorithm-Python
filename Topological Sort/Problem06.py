# https://www.acmicpc.net/problem/1005
import sys
from collections import defaultdict, deque

read = sys.stdin.readline

test = int(read().strip())
while test:
    n, k = map(int, read().strip().split())
    builds = list(map(int, read().strip().split()))
    builds.insert(0, 0)
    times = [0 for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    indegree[0] = -1
    adj = defaultdict(list)
    while k:
        x, y = map(int, read().strip().split())
        adj[x].append(y)
        indegree[y] += 1
        k -= 1
    q = deque()
    for i, e in enumerate(indegree):
        if e == 0:
            q.append(i)
            times[i] = builds[i]

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            indegree[nxt] -= 1
            times[nxt] = max(times[nxt], times[cur] + builds[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
    w = int(read().strip())
    print(times[w])
    test -= 1
