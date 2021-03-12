# https://www.acmicpc.net/problem/5588
import sys

read = sys.stdin.readline
m = int(read().strip())
pivots = [tuple(map(int, read().strip().split())) for _ in range(m)]
pivots.sort()
n = int(read().strip())
stars = [tuple(map(int, read().strip().split())) for _ in range(n)]
stars.sort()
for i in range(n - m + 1):
    px, py = stars[i][0] - pivots[0][0], stars[i][1] - pivots[0][1]
    p_idx = 1
    pivots_x, pivots_y = pivots[p_idx][0] + px, pivots[p_idx][1] + py
    for j in range(i + 1, n):
        if pivots_x == stars[j][0] and pivots_y == stars[j][1]:
            p_idx += 1
            if p_idx == m:
                print(px, py)
                sys.exit()
            pivots_x, pivots_y = pivots[p_idx][0] + px, pivots[p_idx][1] + py
