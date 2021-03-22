# https://www.acmicpc.net/problem/3977
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 1)
read = sys.stdin.readline
test = int(read().strip())


def dfs(cur):
    global idx, sec
    parent[cur] = idx
    s.append(cur)
    ret = idx
    idx += 1

    for nxt in adj[cur]:
        if parent[nxt] == 0:
            ret = min(ret, dfs(nxt))
        elif not finish[nxt]:
            ret = min(ret, parent[nxt])

    if ret == parent[cur]:
        while True:
            e = s.pop()
            sec_nums[e] = sec
            finish[e] = True
            if e == cur:
                break
        sec += 1
    return ret


while test:
    adj = defaultdict(list)
    n, m = map(int, read().strip().split())
    while m:
        a, b = map(int, read().strip().split())
        adj[a].append(b)
        m -= 1

    parent = [0 for _ in range(n)]
    finish = [False for _ in range(n)]
    sec = 0
    sec_nums = [-1] * n
    s = []
    idx = 1

    for i in range(n):
        if parent[i] == 0:
            dfs(i)
    indegree = [0] * sec
    for i in range(n):
        for j in adj[i]:
            if sec_nums[i] != sec_nums[j]:
                indegree[sec_nums[j]] += 1
    cnt = 0
    start = -1
    for i in range(sec):
        if indegree[i] == 0:
            cnt += 1
            start = i

    if cnt > 1:
        print('Confused')
    else:
        for i in range(n):
            if sec_nums[i] == start:
                print(i)
    read().strip()
    print()
    test -= 1

