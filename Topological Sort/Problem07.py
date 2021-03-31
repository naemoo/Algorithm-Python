# https://www.acmicpc.net/problem/14567
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(list)
indegree = [0] * (n + 1)
semesters = [0] * (n + 1)
q = deque()

for _ in range(m):
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, 1))

while q:
    cur, semseter = q.popleft()
    semesters[cur] = semseter

    for nxt in adj[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append((nxt, semseter + 1))

print(*semesters[1:])
