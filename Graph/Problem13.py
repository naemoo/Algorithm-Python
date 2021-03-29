# https://www.acmicpc.net/problem/2152
import sys
from collections import defaultdict, Counter, deque

read = sys.stdin.readline
sys.setrecursionlimit(100006)
n, m, s, t = map(int, read().strip().split())
adj = defaultdict(list)

for _ in range(m):
    st, to = map(int, read().strip().split())
    adj[st].append(to)

parent = [0 for _ in range(n + 1)]
finish = [False for _ in range(n + 1)]
scc = [-1] * (n + 1)
scc_city = Counter()
stack = []
idx = 1
scc_cnt = 0


def dfs(cur):
    global idx, scc_cnt
    parent[cur] = idx
    ret = idx
    stack.append(cur)
    idx += 1

    for nxt in adj[cur]:
        if parent[nxt] == 0:
            ret = min(ret, dfs(nxt))
        elif not finish[nxt]:
            ret = min(ret, parent[nxt])

    if ret == parent[cur]:
        while True:
            e = stack.pop()
            finish[e] = True
            scc[e] = scc_cnt
            scc_city[scc_cnt] += 1
            if e == cur:
                break
        scc_cnt += 1

    return ret


for i in range(1, n + 1):
    if parent[i] == 0:
        dfs(i)

scc_adj = defaultdict(list)
indegree = [0 for _ in range(scc_cnt)]
for a in range(1, n + 1):
    for b in adj[a]:
        if scc[a] != scc[b]:
            nxt = scc[b]
            scc_adj[scc[a]].append(nxt)
            indegree[nxt] += 1


q = deque()
s, t = scc[s], scc[t]
for i in range(scc_cnt):
    if indegree[i] == 0:
        q.append(i)
ans = [0 for _ in range(scc_cnt)]
ans[s] = scc_city[s]
visit = [False for _ in range(scc_cnt)]
visit[s] = True
while q:
    cur = q.popleft()
    for nxt in scc_adj[cur]:
        if visit[cur]:
            ans[nxt] = max(ans[nxt], ans[cur] + scc_city[nxt])
            visit[nxt] = True
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(ans[t])