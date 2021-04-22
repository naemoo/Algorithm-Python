import sys

from collections import defaultdict

adj = defaultdict(list)
ans = 0
sys.setrecursionlimit(300005)


def go(a, cur=0, prev=-1):
    global ans
    if len(adj[cur]) == 1 and adj[cur] == prev:
        return a[cur]
    ret = a[cur]
    for nxt in adj[cur]:
        if nxt != prev:
            tmp = go(a, nxt, cur)
            ans += abs(tmp)
            ret += tmp
    return ret


def solution(a, edges):
    global adj, ans
    adj.clear()
    ans = 0
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # print(ans if go(a) == 0 else -1)
    return ans if go(a) == 0 else -1


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
print(solution([0, 1, 0], [[0, 1], [1, 2]]))
