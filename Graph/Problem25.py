# https://programmers.co.kr/learn/courses/30/lessons/67260
import sys

from collections import defaultdict

sys.setrecursionlimit(200010)


def makeTree(tree, cur, prev, adj):
    if len(adj[cur]) == 1 and adj[cur] == prev:
        return

    for nxt in adj[cur]:
        if nxt == prev:
            continue
        tree[cur].append(nxt)
        makeTree(tree, nxt, cur, adj)


def solution(n, path, order):
    adj = defaultdict(list)
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)
    tree = defaultdict(list)
    makeTree(tree, 0, -1, adj)

    for a, b in order:
        tree[a].append(b)

    scc = []
    parent = [-1] * n
    finish = [False] * n
    s = []
    idx = 0

    def dfs(cur):
        nonlocal idx
        parent[cur] = idx
        ret = idx
        s.append(cur)
        idx += 1
        for nxt in tree[cur]:
            if parent[nxt] == -1:
                ret = min(ret, dfs(nxt))
            elif not finish[nxt]:
                ret = min(ret, parent[nxt])

        if ret == parent[cur]:
            tmp = []
            while True:
                e = s.pop()
                finish[e] = True
                tmp.append(e)
                if cur == e:
                    break
            if len(tmp) > 1:
                scc.append(tmp)
        return ret

    for i in range(n):
        if parent[i] == -1:
            dfs(i)

    return False if scc else True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
