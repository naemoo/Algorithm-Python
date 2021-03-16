# https://www.acmicpc.net/problem/2001
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
jewels = dict(zip([int(read().strip()) for _ in range(k)], range(k)))
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
visit = [[False for _ in range(n + 1)] for _ in range(1 << k)]

while m:
    a, b, c = map(int, read().strip().split())
    adj[a][b] = c
    adj[b][a] = c
    m -= 1

ans = 0


def go(state, cur, cnt):
    global ans
    visit[state][cur] = True
    if cur == 1:
        ans = max(ans, cnt)

    for nxt, weight in adj[cur].items():
        if not visit[state][nxt] and cnt <= weight:
            go(state, nxt, cnt)
        if nxt in jewels.keys():
            if state & (1 << jewels[nxt]):
                continue
            ns = state | (1 << jewels[nxt])
            if not visit[ns][nxt] and cnt + 1 <= weight:
                go(ns, nxt, cnt + 1)


adj[1][1] = 100
go(0, 1, 0)
print(ans)
