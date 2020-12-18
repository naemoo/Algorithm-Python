# https://www.acmicpc.net/problem/1949
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n = int(input())
villages = list(map(int, input().strip().split()))
tree = defaultdict(list)

for _ in range(n - 1):
    st, to = map(int, input().strip().split())
    tree[st].append(to)
    tree[to].append(st)

dp = [None for _ in range(n + 1)]
visit = [True] * (n + 1)

def dfs(cur):
    sum = [0, villages[cur - 1]]
    for nxt in tree[cur]:
        if visit[nxt]:
            visit[nxt] = False
            n0, n1 = dfs(nxt)
            sum[0] += max(n0, n1)
            sum[1] += n0
    dp[cur] = sum
    return sum

visit[1] = False
dfs(1)
print(max(dp[1]))
