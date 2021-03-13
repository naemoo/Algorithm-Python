# https://www.acmicpc.net/problem/1574
import sys
from collections import defaultdict

read = sys.stdin.readline
r, c, n = map(int, read().strip().split())
adj = defaultdict(lambda: set(range(1, c + 1)))

for _ in range(n):
    a, b = map(int, read().strip().split())
    if b in adj[a]:
        adj[a].remove(b)
rook = [0 for _ in range(c + 1)]

def play(cur):
    for nxt in adj[cur]:
        if visit[nxt]:
            continue
        visit[nxt] = True

        if rook[nxt] == 0 or play(rook[nxt]):
            rook[nxt] = cur
            return True
    return False


for i in range(1, r + 1):
    visit = [False for _ in range(c + 1)]
    play(i)

ans = 0
for e in rook:
    if e:
        ans += 1

print(ans)