# https://www.acmicpc.net/problem/1981
import sys
from collections import deque
from itertools import chain

read = sys.stdin.readline
n = int(read().strip())
arr = [list(map(int, read().strip().split())) for _ in range(n)]
s = sorted(set(chain(*arr)))

start = 0
end = 0
ans = float('inf')
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def canGo(st, to):
    q = deque()
    q.append((0, 0))
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[0][0] = True

    while q:
        x, y = q.popleft()

        if st > arr[x][y] or arr[x][y] > to:
            continue

        if x == n - 1 and y == n - 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny]:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

    return False


for start in range(len(s)):
    while end < len(s) and not canGo(s[start], s[end]):
        end += 1
    if end < len(s):
        ans = min(ans, s[end] - s[start])

print(ans)
