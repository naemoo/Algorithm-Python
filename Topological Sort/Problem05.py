# https://www.acmicpc.net/problem/3665
import sys
from collections import defaultdict, Counter, deque

read = sys.stdin.readline
test = int(read().strip())
while test:
    n = int(read().strip())
    teams = list(map(int, read().strip().split()))
    team_to_rank = dict(zip(teams, range(1, n + 1)))
    rank_to_team = dict(zip(range(1, n + 1), teams))
    adj = defaultdict(set)
    indegree = Counter()

    for i in range(n, 0, -1):
        for j in range(1, i):
            adj[rank_to_team[i]].add(rank_to_team[j])
            indegree[rank_to_team[j]] += 1
    m = int(read().strip())
    while m:
        a, b = map(int, read().strip().split())
        if b in adj[a]:
            adj[a].remove(b)
            indegree[b] -= 1
            adj[b].add(a)
            indegree[a] += 1
        else:
            adj[b].remove(a)
            indegree[a] -= 1
            adj[a].add(b)
            indegree[b] += 1
        m -= 1
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    ans = []
    while q:
        if len(q) > 1:
            print('?')
            break

        cur = q.popleft()
        ans.append(cur)
        for nxt in adj[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    if len(ans) == n:
        while ans:
            print(ans.pop(), end=' ')
        print()
    else:
        print('IMPOSSIBLE')
    test -= 1
