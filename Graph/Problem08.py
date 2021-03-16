# https://www.acmicpc.net/problem/1506
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
costs = list(map(int, read().strip().split()))
costs.insert(0, 0)
adj = defaultdict(list)

for i in range(1, n + 1):
    for j, e in enumerate(map(int, list(read().strip())), start=1):
        if e:
            adj[i].append(j)

scc = []
s = []
parent = [0] * (n + 1)
finish = [False] * (n + 1)
idx = 0


def dfs(cur):
    global idx
    idx += 1
    parent[cur] = idx
    s.append(cur)
    ret = parent[cur]

    for nxt in adj[cur]:
        if parent[nxt] == 0:
            ret = min(ret, dfs(nxt))
        elif not finish[nxt]:
            ret = min(ret, parent[nxt])

    if ret == parent[cur]:
        tmp = []
        while True:
            e = s.pop()
            tmp.append(e)
            finish[e] = True
            if cur == e:
                break
        scc.append(tmp)
    return ret


for i in range(1, n + 1):
    if not parent[i]:
        dfs(i)

ans = 0
for e in scc:
    cost = float('inf')
    for police in e:
        cost = min(cost, costs[police])
    ans += cost
print(ans)

