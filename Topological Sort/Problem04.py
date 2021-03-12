# https://www.acmicpc.net/problem/2623
import sys
from collections import Counter, defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(list)
indegrees = Counter()

for _ in range(m):
    iter = list(map(int, read().strip().split()))
    for i, e in enumerate(iter[1:]):
        if i:
            adj[iter[i]].append(e)
            indegrees[e] += 1

q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

ans = []

while q:
    cur = q.popleft()
    ans.append(cur)
    for nxt in adj[cur]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)

if len(ans) == n:
    for e in ans:
        print(e)
else:
    print(0)
