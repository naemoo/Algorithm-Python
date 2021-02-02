# https://www.acmicpc.net/problem/1516
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n = int(read().strip())
q = deque()
buildings = defaultdict(list)
times = [0 for _ in range(n + 1)]
ret = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
idx = 1

while n:
    tmp = tuple(map(int, read().strip().split()))
    if len(tmp) == 2:
        times[idx] = tmp[0]
        ret[idx] = tmp[0]
        q.append(idx)
    else:
        time = tmp[0]
        times[idx] = time
        for e in tmp[1:]:
            if e > 0:
                buildings[e].append(idx)
                indegree[idx] += 1
    idx += 1
    n -= 1

while q:
    cur = q.popleft()

    for nxt in buildings[cur]:
        indegree[nxt] -= 1
        ret[nxt] = max(ret[cur] + times[nxt], ret[nxt])
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, len(ret)):
    print(ret[i])
