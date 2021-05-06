# https://www.acmicpc.net/problem/17143
import sys

read = sys.stdin.readline
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
r, c, m = map(int, read().strip().split())
pools = [[None for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, read().strip().split())
    pools[x - 1][y - 1] = [s, d - 1, z]
ans = 0
for fisher in range(c):
    for i in range(r):
        if pools[i][fisher]:
            ans += pools[i][fisher][2]
            pools[i][fisher] = None
            break

    nxt_sharks = []

    for x in range(r):
        for y in range(c):
            if pools[x][y]:
                s, d, z = pools[x][y]
                pools[x][y] = None
                s = s % (2 * (r - 1)) if d < 2 else s % (2 * (c - 1))
                i, j = x, y
                for _ in range(s):
                    dx, dy = directions[d]
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        d = 1 - d if d < 2 else 2 + (3 - d)
                    dx, dy = directions[d]
                    i, j = i + dx, j + dy
                nxt_sharks.append((i, j, s, d, z))

    for x, y, s, d, z in nxt_sharks:
        if pools[x][y]:
            if z > pools[x][y][2]:
                pools[x][y] = (s, d, z)
        else:
            pools[x][y] = (s, d, z)

print(ans)
