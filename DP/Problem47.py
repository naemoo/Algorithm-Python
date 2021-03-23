# https://www.acmicpc.net/problem/2079
import sys
from collections import defaultdict
from heapq import heappop, heappush

read = sys.stdin.readline
word = read().strip()
n = len(word)
palindrome = [[-1 for _ in range(n)] for _ in range(n)]


def go(start, end):
    if start >= end:
        return True

    if palindrome[start][end] != -1:
        return palindrome[start][end]

    if word[start] == word[end]:
        ret = go(start + 1, end - 1)
    else:
        ret = False

    palindrome[start][end] = ret
    return ret


adj = defaultdict(list)

for i in range(n):
    palindrome[i][i] = True
    adj[i].append(i + 1)
    for j in range(i + 1, n):
        if go(i, j):
            adj[i].append(j + 1)

q = [(0, 0)]
visit = [float('inf') for _ in range(n + 1)]
visit[0] = 0

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
