# https://www.acmicpc.net/problem/11266
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 1)
read = sys.stdin.readline
n, e = map(int, read().strip().split())
visit_order = [0 for _ in range(n + 1)]
ans = set()
adj = defaultdict(list)
num = 1
cnt = 0

while e:
    st, to = map(int, read().strip().split())
    adj[st].append(to)
    adj[to].append(st)
    e -= 1


def dfs(cur, parent, isRoot=False):
    global num, cnt
    visit_order[cur] = num
    num += 1
    ret = visit_order[cur]
    child = 0
    for nxt in adj[cur]:
        if nxt == parent:
            continue
        if visit_order[nxt]:
            ret = min(ret, visit_order[nxt])
        else:
            child += 1
            df = dfs(nxt, cur)
            if not isRoot and visit_order[cur] <= df:
                ans.add(cur)
            ret = min(df, ret)
    if isRoot and child > 1:
        ans.add(cur)
        cnt += 1

    return ret


for i in range(1, n):
    if not visit_order[i]:
        dfs(i, 0, True)

print(len(ans))
for i in range(n + 1):
    if i in ans:
        print(i, end=' ')
