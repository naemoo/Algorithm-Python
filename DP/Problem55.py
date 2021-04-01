# https://www.acmicpc.net/problem/16991
import math
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
villages = [list(map(int, read().strip().split())) for _ in range(n)]
all = (1 << n) - 1
adj = defaultdict(lambda: defaultdict(lambda: float('inf')))
dp = [[[-1 for _ in range(1 << n)] for _ in range(n)] for _ in range(n)]


def getDistance(dept, arrival):
    return math.sqrt(pow(dept[0] - arrival[0], 2) + pow(dept[1] - arrival[1], 2))


for i, village in enumerate(villages):
    for j, e in enumerate(villages):
        if i != j:
            adj[i][j] = getDistance(village, e)


def go(start, cur, state):
    global all
    if state == all:
        return adj[cur][start]
    if dp[start][cur][state] != -1:
        return dp[start][cur][state]

    ret = float('inf')
    for nxt, nw in adj[cur].items():
        if state & (1 << nxt) == 0:
            ret = min(ret, go(start, nxt, state | (1 << nxt)) + adj[cur][nxt])
    dp[start][cur][state] = ret
    return ret


ans = float('inf')
for i in range(n):
    ans = min(ans, go(i, i, 1 << i))

print(ans)
