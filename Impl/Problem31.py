# https://www.acmicpc.net/problem/20056
import sys
from collections import defaultdict

read = sys.stdin.readline
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
odd_dir = (1, 3, 5, 7)
even_dir = (0, 2, 4, 6)
n, m, k = map(int, read().strip().split())
fires = []
for _ in range(m):
    r, c, m, s, d = map(int, read().strip().split())
    fires.append((r - 1, c - 1, m, s, d))

for _ in range(k):
    new_fires = defaultdict(list)
    while fires:
        x, y, m, s, d = fires.pop()
        dx, dy = directions[d]
        nx, ny = (n + x + dx * s) % n, (n + y + dy * s) % n
        new_fires[(nx, ny)].append((m, s, d))

    for (x, y), v in new_fires.items():
        if len(v) > 1:
            isEven = False if v[0][-1] % 2 else True
            isSame = True
            weight = 0
            velocity = 0
            for m, s, d in v:
                weight += m
                velocity += s
                if d % 2 and isEven:
                    isSame = False
                elif d % 2 == 0 and not isEven:
                    isSame = False
            nxt_dir = even_dir if isSame else odd_dir
            nw = weight // 5
            nv = velocity // len(v)
            if nw:
                for i in nxt_dir:
                    fires.append((x, y, nw, nv, i))
        else:
            fires.append((x, y, *v[0]))

print(sum(map(lambda x: x[2], fires)))
