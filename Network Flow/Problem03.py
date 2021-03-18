# https://www.acmicpc.net/problem/11375
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(list)
for i in range(1, n + 1):
    adj[i].extend(list(map(int, read().strip().split()[1:])))

works = [0 for _ in range(m + 1)]


def dfs(cur):
    for nxt in adj[cur]:
        if visit[nxt]:
            continue
        visit[nxt] = True

        if works[nxt] == 0 or dfs(works[nxt]):
            works[nxt] = cur
            return True
    return False


for i in range(1, n + 1):
    visit = [False for _ in range(m + 1)]
    dfs(i)

print(len(list(filter(lambda x: x != 0, works))))
