# https://www.acmicpc.net/problem/1135
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
adj = defaultdict(list)
times = [0 for _ in range(51)]

for i, e in enumerate(list(map(int, read().strip().split()))):
    if i:
        adj[e].append(i)


def go(cur):
    ret = 0
    for nxt in adj[cur]:
        times[nxt] = go(nxt) + 1
    adj[cur].sort(key=lambda x: -times[x])
    for i, nxt in enumerate(adj[cur]):
        times[nxt] += i
        ret = max(ret, times[nxt])
    return ret

print(go(0))