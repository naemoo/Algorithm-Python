# https://www.acmicpc.net/problem/14442
import sys
from collections import deque

read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
mazes = [read().strip() for _ in range(n)]
q = deque([(0, 0, 1, 0)])
visit[0][0][0] = True

while q:
    x, y, d, w = q.popleft()

    if (x, y) == (n - 1, m - 1):
        print(d)
        sys.exit()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[w][nx][ny]:
            continue

        if mazes[nx][ny] == '1' and w < k and not visit[w + 1][nx][ny]:
            q.append((nx, ny, d + 1, w + 1))
            visit[w + 1][nx][ny] = True
        elif mazes[nx][ny] == '0':
            q.append((nx, ny, d + 1, w))
            visit[w][nx][ny] = True

print(-1)
