# https://www.acmicpc.net/problem/15681
import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,r,q = map(int,input().strip().split())
tree = defaultdict(list)
for _ in range(n-1):
    u,v = map(int,input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

visit = [True] * (n+1)
visit[r] = False
dp = [-1] * (n+1)
def dfs(start):
    cnt = 1
    for nxt in tree[start]:
        if visit[nxt]:
            visit[nxt] = False
            cnt += dfs(nxt)
    dp[start] = cnt
    return cnt

dfs(r)

for _ in range(q):
    subRoot = int(input().strip())
    print(dp[subRoot])
