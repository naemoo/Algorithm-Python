# https://www.acmicpc.net/problem/2157
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
adj = defaultdict(list)

while k:
    a, b, c = map(int, read().strip().split())
    if a < b:
        adj[a].append((b, c))
    k -= 1

dp = [[-1 for _ in range(m + 1)] for _ in range(n)]


def go(cur, cnt):
    if cur == n:
        return 0

    if dp[cur][cnt] != -1:
        return dp[cur][cnt]

    ret = -float('inf')
    for nxt, w in adj[cur]:
        if cnt + 1 <= m:
            ret = max(ret, go(nxt, cnt + 1) + w)
    dp[cur][cnt] = ret
    return ret


print(go(1, 1))
