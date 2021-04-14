# https://www.acmicpc.net/problem/17471
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n = int(read().strip())
cities = list(map(int, read().strip().split()))
cities.insert(0, 0)
adj = defaultdict(set)

for i in range(1, n + 1):
    for e in map(int, read().strip().split()[1:]):
        adj[i].add(e)
        adj[e].add(i)
ans = float('inf')


def isAllContected(sec):
    start = list(sec)[0]
    q = deque([start])
    visit = set()
    visit.add(start)
    while q:
        cur = q.popleft()

        for nxt in adj[cur]:
            if nxt in visit or nxt not in sec:
                continue
            q.append(nxt)
            visit.add(nxt)

    return True if visit == sec else False


for i in range(1 << n):
    a_section = set()
    b_section = set()

    for j in range(n):
        if i & (1 << j):
            a_section.add(j + 1)
        else:
            b_section.add(j + 1)

    if len(a_section) == 0 or len(b_section) == 0:
        continue

    if isAllContected(a_section) and isAllContected(b_section):
        a_total = sum(map(lambda x: cities[x], a_section))
        b_total = sum(map(lambda x: cities[x], b_section))
        ans = min(ans, abs(a_total - b_total))
print(ans if ans != float('inf') else -1)
