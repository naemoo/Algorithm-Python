# https://www.acmicpc.net/problem/17831
import sys
from collections import defaultdict
sys.setrecursionlimit(20 ** 5)
input = sys.stdin.readline
n = int(input().strip())
tree = defaultdict(list)
for st, to in enumerate(map(int, input().strip().split())):
    tree[to - 1].append(st + 1)
synergy = [syn for syn in map(int,input().strip().split())]

dp = [None for _ in range(n)]

def dfs(cur):
    if dp[cur] != None:
        return dp[cur]
    total = [0,0]
    for nxt in tree[cur]:
        total[1] += dfs(nxt)[0]

    for nxt in tree[cur]:
        tmp = total[1] - dfs(nxt)[0] + dfs(nxt)[1] + (synergy[nxt] * synergy[cur])
        total[0] = max(total[0],tmp)
    total[0] = max(total)
    dp[cur] = total
    return dp[cur]
print(max(dfs(0)))