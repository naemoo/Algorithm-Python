# https://www.acmicpc.net/problem/15685
import sys

read = sys.stdin.readline
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
n = int(read().strip())
dragon_curves = [list(map(int, read().strip().split())) for _ in range(n)]
points = set()


def rotate(point, pivot):
    px, py = pivot
    x, y = point
    ny = py + x - px
    nx = px - (y - py)
    return nx, ny


for x, y, d, g in dragon_curves:
    dx, dy = directions[d]
    last = (x + dx, y + dy)
    start = (x, y)
    generation = set([start, last])
    for _ in range(g):
        tmp = set()
        for point in generation:
            tmp.add(rotate(point, last))
        last = rotate(start, last)
        generation = generation.union(tmp)

    for e in generation:
        points.add(e)
ans = 0
for px, py in points:
    if (px + 1, py) in points and (px, py + 1) in points and (px + 1, py + 1) in points:
        ans += 1
print(ans)