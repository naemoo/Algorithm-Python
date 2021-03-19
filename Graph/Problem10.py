# https://www.acmicpc.net/problem/4196
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 5)
read = sys.stdin.readline
test = int(read().strip())


def dfs(cur):
    global idx, cnt
    ret = idx
    s.append(cur)
    parent[cur] = ret
    idx += 1

    for nxt in adj[cur]:
        if parent[nxt] == 0:
            ret = min(dfs(nxt), ret)
        elif not finish[nxt]:
            ret = min(parent[nxt], ret)

    if parent[cur] == ret:
        while True:
            e = s.pop()
            finish[e] = True
            scc_num[e] = cnt
            if cur == e:
                break
        cnt += 1
    return ret


while test:
    n, m = map(int, read().strip().split())
    adj = defaultdict(list)
    scc = []
    scc_num = [0 for _ in range(n + 1)]
    cnt = 1
    s = []
    idx = 1
    parent = [0 for _ in range(n + 1)]
    finish = [False for _ in range(n + 1)]

    while m:
        a, b = map(int, read().strip().split())
        adj[a].append(b)
        m -= 1

    for i in range(1, n + 1):
        if parent[i] == 0:
            dfs(i)

    indegree = [0 for _ in range(cnt)]

    for i in range(1, n + 1):
        for j in adj[i]:
            if scc_num[i] != scc_num[j]:
                indegree[scc_num[j]] += 1

    ans = 0
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            ans += 1
    print(ans)
    test -= 1
