# https://www.acmicpc.net/problem/1865
import sys
from collections import defaultdict

read = sys.stdin.readline
tc = int(read().strip())
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))


def bel():
    visit = [10**9 for _ in range(n + 1)]
    flag = False
    for _ in range(n - 1):
        for cur in adj.keys():
            for nxt, w1 in adj[cur].items():
                if visit[nxt] > w1 + visit[cur]:
                    visit[nxt] = w1 + visit[cur]
    for cur in adj.keys():
        for nxt, w1 in adj[cur].items():
            if visit[nxt] > w1 + visit[cur]:
                flag = True
    print(visit)
    return flag


while tc:
    n, m, w = map(int, read().strip().split())
    while m:
        s, e, t = map(int, read().strip().split())
        adj[s][e] = min(adj[s][e], t)
        adj[e][s] = min(adj[e][s], t)
        m -= 1
    while w:
        s, e, t = map(int, read().strip().split())
        adj[s][e] = -t
        w -= 1

    flag = False
    flag = bel()

    if flag:
        print('YES')
    else:
        print('NO')
    adj.clear()
    tc -= 1
