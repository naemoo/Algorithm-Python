# https://www.acmicpc.net/problem/13913
import sys
from collections import deque

read = sys.stdin.readline
max_pos = 100000 * 2
directions = (1, -1, 0)
n, k = map(int, read().strip().split())

visit = [-1 for _ in range(max_pos)]
path = [None for _ in range(max_pos)]
q = deque()
if n != k:
    q.append((n, 0))
visit[n] = 0

while q:
    cur, d = q.popleft()

    for dir in directions:
        if not dir:
            nxt = cur * 2
        else:
            nxt = cur + dir

        if nxt < 0 or nxt >= max_pos or visit[nxt] != -1:
            continue
        q.append((nxt, d + 1))
        visit[nxt] = d + 1
        path[nxt] = cur
        if nxt == k:
            q.clear()
            break
print(visit[k])
cur = k
ans = []
while cur != None:
    ans.append(cur)
    cur = path[cur]
while ans:
    print(ans.pop(), end=' ')
