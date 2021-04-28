# https://www.acmicpc.net/problem/2213
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
sys.setrecursionlimit(10005)
n = int(read().strip())
vertex = list(map(int, read().strip().split()))
vertex.insert(0, 0)
adj = defaultdict(list)
tree = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque([(1, -1)])
while q:
    cur, prev = q.popleft()

    for nxt in adj[cur]:
        if nxt == prev:
            continue
        q.append((nxt, cur))
        tree[cur].append(nxt)

dp = [[None for _ in range(2)] for _ in range(n + 1)]


def getMax(cur):
    ret = [0, vertex[cur]]
    for nxt in tree[cur]:
        tmp = getMax(nxt)
        ret[0] += max(tmp)
        ret[1] += tmp[0]
    dp[cur] = ret
    return ret


def getPath(cur, parent):
    if parent:
        for nxt in tree[cur]:
            getPath(nxt, 0)
    else:
        for nxt in tree[cur]:
            now = 1 if dp[nxt][0] < dp[nxt][1] else 0
            if now:
                path.append(nxt)
            getPath(nxt, now)


print(max(getMax(1)))
path = []
t = 1 if dp[1][0] < dp[1][1] else 0
if t:
    path.append(1)
getPath(1, t)
path.sort()
print(*path)