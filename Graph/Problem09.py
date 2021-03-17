# https://www.acmicpc.net/problem/9466
import sys

sys.setrecursionlimit(10 ** 5 + 5)
read = sys.stdin.readline
test = int(read().strip())


def dfs(cur):
    global idx
    idx += 1
    s.append(cur)
    parent[cur] = idx
    ret = idx
    nxt = adj[cur]
    if parent[nxt] == 0:
        ret = min(ret, dfs(nxt))
    elif not finish[nxt]:
        ret = min(ret, parent[nxt])

    if parent[cur] == ret:
        tmp = []
        while True:
            e = s.pop()
            tmp.append(e)
            finish[e] = True
            if e == cur:
                break
        scc.append(tmp)

    return ret


while test:
    n = int(read().strip())
    parent = [0] * (n + 1)
    finish = [False] * (n + 1)
    scc = []
    s = []
    idx = 0
    adj = list(map(int, read().strip().split()))
    adj.insert(0, 0)

    for i in range(1, n + 1):
        if parent[i] == 0:
            dfs(i)

    cnt = 0
    for e in scc:
        if len(e) == 1 and adj[e[0]] == e[0]:
            cnt += 1
        elif len(e) > 1:
            cnt += len(e)
    print(n - cnt)
    test -= 1
