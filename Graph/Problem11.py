# https://www.acmicpc.net/problem/15783
import sys
from collections import defaultdict

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 5)
n, m = map(int, read().strip().split())
adj = defaultdict(list)

for _ in range(m):
    a, b = map(int, read().strip().split())
    adj[a].append(b)

idx = 1
parent = [0 for _ in range(n)]
finish = [False for _ in range(n)]
s = []
s_cnt = 0
s_nums = [-1 for _ in range(n)]


def getSection(cur):
    global idx, s_cnt
    parent[cur] = idx
    ret = idx
    s.append(cur)
    idx += 1

    for nxt in adj[cur]:
        if parent[nxt] == 0:
            ret = min(ret, getSection(nxt))
        elif not finish[nxt]:
            ret = min(ret, parent[nxt])

    if parent[cur] == ret:
        while True:
            e = s.pop()
            s_nums[e] = s_cnt
            finish[e] = True
            if e == cur:
                break
        s_cnt += 1
    return ret


for i in range(n):
    if parent[i] == 0:
        getSection(i)

indegree = [0] * (s_cnt)

for i in range(n):
    for j in adj[i]:
        if s_nums[i] != s_nums[j]:
            indegree[s_nums[j]] += 1

print(len(list(filter(lambda x: x == 0, indegree))))
