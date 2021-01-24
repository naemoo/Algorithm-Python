# https://www.acmicpc.net/problem/2533
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
inp = sys.stdin.readline
n = int(inp().strip())
tree = defaultdict(list)
for _ in range(n - 1):
    st, to = list(map(int, inp().strip().split()))
    tree[st - 1].append(to - 1)
    tree[to - 1].append(st - 1)

dp = [None for _ in range(n + 1)]
visit = [[True for _ in range(n)] for _ in range(n)]

def getEarlyAdapter(cur):
    if dp[cur] != None:
        return dp[cur]

    ret = [0,1]
    for nxt in tree[cur]:
        if visit[nxt]:
            visit[nxt] = False
            getEarlyAdapter(nxt)
            ret[0] += dp[nxt][1]
            ret[1] += min(dp[nxt][0],dp[nxt][1])

    dp[cur] = ret
    return dp[cur]

visit[0] = False
print(min(getEarlyAdapter(0)))