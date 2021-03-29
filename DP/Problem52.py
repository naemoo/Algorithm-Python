# https://www.acmicpc.net/problem/1029
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
adj = defaultdict(list)
for i in range(n):
    for j, e in enumerate(map(int, read().strip())):
        if i != j:
            adj[i].append((j, e))

dp = [[[-1 for _ in range(1 << 15)] for _ in range(10)] for _ in range(15)]


def go(cur, prev, state):
    if dp[cur][prev][state] != -1:
        return dp[cur][prev][state]

    ret = 0
    for nxt, cost in adj[cur]:
        if (state & (1 << nxt)) == 0 and prev <= cost:
            ret = max(ret, go(nxt, cost, state | (1 << nxt)) + 1)
    dp[cur][prev][state] = ret
    return ret


print(go(0, 0, 1) + 1)
