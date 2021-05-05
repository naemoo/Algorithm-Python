# https://www.acmicpc.net/problem/19237
import sys
from collections import defaultdict

read = sys.stdin.readline
directions = (None, (-1, 0), (1, 0), (0, -1), (0, 1))
n, m, k = map(int, read().strip().split())
pools = [list(map(int, read().strip().split())) for _ in range(n)]
smells = [[None for _ in range(n)] for _ in range(n)]
sharks_dir = list(map(int, read().strip().split()))  # 각 상어 방향
sharks_dir.insert(0, None)
sharks_pri = defaultdict(lambda: [None])
sharks_loc = list(
    map(lambda x: [x // n, x % n, pools[x // n][x % n]], filter(lambda x: pools[x // n][x % n], range(n ** 2))))

for sh in range(1, len(sharks_dir) + 1):
    for _ in range(4):
        sharks_pri[sh].append(list(map(int, read().strip().split())))

ans = 0
while sum(map(sum, pools)) != 1 and ans <= 1000:
    for x, y, z in sharks_loc:
        smells[x][y] = [z, k]

    nxt_sharks = []
    for x, y, z in sharks_loc:
        flag = False
        pools[x][y] = 0
        for d in sharks_pri[z][sharks_dir[z]]:
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not smells[nx][ny]:
                nxt_sharks.append((nx, ny, z, d))
                flag = True
                break

        if flag:
            continue

        for d in sharks_pri[z][sharks_dir[z]]:
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if smells[nx][ny][0] == z:
                nxt_sharks.append((nx, ny, z, d))
                break

    sharks_loc = []
    for x, y, z, d in nxt_sharks:
        sharks_dir[z] = d
        sharks_loc.append((x, y, z))
        if pools[x][y]:
            sharks_loc.remove((x, y, max(z, pools[x][y])))
            pools[x][y] = min(pools[x][y], z)
        else:
            pools[x][y] = z

    for x in range(n):
        for y in range(n):
            if smells[x][y]:
                smells[x][y][1] -= 1
                if smells[x][y][1] == 0:
                    smells[x][y] = None

    ans += 1
print(ans if ans <= 1000 else -1)
