# https://www.acmicpc.net/problem/1509
import sys
from heapq import heappop, heappush
from collections import defaultdict

read = sys.stdin.readline
word = read().strip()
n = len(word)
sys.setrecursionlimit(2505)
dp = [[None for _ in range(n)] for _ in range(n)]


def isPalindrome(start, end):
    if start >= end:
        if start == end:
            dp[start][end] = True
        return True

    if dp[start][end] != None:
        return dp[start][end]

    ret = None
    if word[start] == word[end]:
        ret = isPalindrome(start + 1, end - 1)
    else:
        ret = False
    dp[start][end] = ret
    return ret


adj = defaultdict(list)

for i in range(n):
    for j in range(i, n):
        if isPalindrome(i, j):
            adj[i].append(j + 1)

visit = [float('inf') for _ in range(n + 1)]
visit[0] = 0
q = [(0, 0)]
while q:
    cost, cur = heappop(q)

    if visit[cur] < cost:
        continue

    for nxt in adj[cur]:
        nxt_cost = cost + 1
        if nxt_cost < visit[nxt]:
            heappush(q, (nxt_cost, nxt))
            visit[nxt] = nxt_cost
print(visit[n])
