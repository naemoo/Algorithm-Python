# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

read = sys.stdin.readline
n = int(read().strip())
pools = [list(map(int, read().strip().split())) for _ in range(n)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i, pool in enumerate(pools):
    for j, e in enumerate(pool):
        if e == 9:
            shark = (i, j)


def getFish(cur, size):
    ret = []
    q = deque([[*cur, 0]])
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[cur[0]][cur[1]] = True
    while q:
        x, y, d = q.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visit[nx][ny]:
                continue
            if size < pools[nx][ny]:
                continue
            nd = d + 1
            if pools[nx][ny]:
                if ret and ret[-1][2] < nd:
                    return ret
                elif pools[nx][ny] < size:
                    ret.append((nx, ny, nd))
            q.append((nx, ny, nd))
            visit[nx][ny] = True

    return ret


ans = 0
cur_size = 2
cur_cnt = 0
while fish := getFish(shark, cur_size):
    fish.sort(key=lambda x: (x[2], x[0], x[1]), reverse=True)
    nxt_shark = fish.pop()
    x, y = shark
    pools[x][y] = 0
    shark = (nxt_shark[0], nxt_shark[1])
    cur_cnt += 1
    if cur_cnt == cur_size:
        cur_size += 1
        cur_cnt = 0
    ans += nxt_shark[2]
print(ans)
