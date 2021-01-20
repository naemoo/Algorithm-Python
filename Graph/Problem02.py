# https://www.acmicpc.net/problem/2458
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
graph = defaultdict(list)
revGraph = defaultdict(list)
counts = [0 for _ in range(n + 1)]

while m:
    s1, s2 = map(int, read().strip().split())
    graph[s1].append(s2)
    revGraph[s2].append(s1)
    m -= 1

ret = 0
for i in range(1, n + 1):
    tmp = 0
    q = deque()
    visit = [False for _ in range(n + 1)]
    visit[i] = True
    q.append(i)
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visit[nxt]:
                q.append(nxt)
                visit[nxt] = True
                tmp += 1

    q = deque()
    visit = [False for _ in range(n + 1)]
    visit[i] = True
    q.append(i)
    while q:
        cur = q.popleft()
        for nxt in revGraph[cur]:
            if not visit[nxt]:
                q.append(nxt)
                visit[nxt] = True
                tmp += 1
    counts[i] += tmp

ret = 0
for cnt in counts:
    if cnt == n - 1:
        ret += 1
print(ret)
