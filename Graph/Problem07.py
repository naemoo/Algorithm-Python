# https://www.acmicpc.net/problem/2150
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4 + 5)
read = sys.stdin.readline
v, e = map(int, read().strip().split())
adj = defaultdict(list)
finish = [False for _ in range(v + 1)]
d = [0 for _ in range(v + 1)]
s = []
idx = 0
scc = []

for _ in range(e):
    a, b = map(int, read().strip().split())
    adj[a].append(b)


def go(cur):
    global idx
    idx += 1
    d[cur] = idx
    parent = d[cur]
    s.append(cur)

    for nxt in adj[cur]:
        if d[nxt] == 0:
            parent = min(parent, go(nxt))
        elif not finish[nxt]:
            parent = min(parent, d[nxt])

    if d[cur] == parent:
        ret = []
        while True:
            element = s.pop()
            ret.append(element)
            finish[element] = True
            if element == cur:
                break
        scc.append(sorted(ret))
    return parent


for i in range(1, v + 1):
    if d[i] == 0:
        go(i)

scc.sort()
print(len(scc))
for element in scc:
    for ans in element:
        print(ans, end=' ')
    print(-1)
