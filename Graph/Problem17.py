# https://www.acmicpc.net/problem/4013
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
sys.setrecursionlimit(500010)
n, m = map(int, read().strip().split())
adj = defaultdict(list)

while m:
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    m -= 1

atms = [int(read().strip()) for _ in range(n)]
start, p = map(int, read().strip().split())
restaurant = set(map(int, read().strip().split()))

idx = 1
s = []
scc_cnt = 0
scc_atm = {}
scc = [-1 for _ in range(n + 1)]
finish = [False for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]


def dfs(cur):
    global idx, scc_cnt
    parent[cur] = idx
    s.append(cur)
    ret = idx
    idx += 1
    for nxt in adj[cur]:
        if parent[nxt] == -1:
            ret = min(ret, dfs(nxt))
        elif not finish[nxt]:
            ret = min(ret, parent[nxt])

    if ret == parent[cur]:
        tmp = 0
        while True:
            e = s.pop()
            tmp += atms[e - 1]
            scc[e] = scc_cnt
            finish[e] = True
            if e == cur:
                break
        scc_atm[scc_cnt] = tmp
        scc_cnt += 1
    return ret


for i in range(1, n + 1):
    if parent[i] == -1:
        dfs(i)

scc_adj = defaultdict(list)
indegree = [0 for _ in range(scc_cnt)]

for st in adj:
    for to in adj[st]:
        if scc[st] != scc[to]:
            scc_adj[scc[st]].append(scc[to])
            indegree[scc[to]] += 1

q = deque()
for i in range(scc_cnt):
    if indegree[i] == 0:
        q.append(i)
dp = [0 for _ in range(scc_cnt)]
dp[scc[start]] = scc_atm[scc[start]]
visit = [False for _ in range(scc_cnt)]
visit[scc[start]] = True

while q:
    cur = q.popleft()

    for nxt in scc_adj[cur]:
        if visit[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + scc_atm[nxt])
            visit[nxt] = True
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

ans = 0
for e in restaurant:
    ans = max(ans, dp[scc[e]])
print(ans)
