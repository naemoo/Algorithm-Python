# https://www.acmicpc.net/problem/2819
import sys
from bisect import bisect_left, bisect_right

read = sys.stdin.readline
n, m = map(int, read().strip().split())
sensors = [tuple(map(int, read().strip().split())) for _ in range(n)]
directions = {'S': (0, 1), 'I': (1, 0), 'J': (0, -1), 'Z': (-1, 0)}
x_pos = sorted(map(lambda x: x[0], sensors))
y_pos = sorted(map(lambda x: x[1], sensors))
x_sum = [0 for _ in range(n + 1)]
y_sum = [0 for _ in range(n + 1)]
for i in range(n):
    x_sum[i + 1] = x_sum[i] + x_pos[i]
    y_sum[i + 1] = y_sum[i] + y_pos[i]

x, y = (0, 0)
for cmd in read().strip():
    ans = 0
    dx, dy = directions[cmd]
    nx, ny = x + dx, y + dy
    xl_idx = bisect_left(x_pos, nx)
    xh_idx = bisect_right(x_pos, nx)
    left = max(xl_idx * nx - x_sum[xl_idx], 0)
    right = max(0, x_sum[n] - x_sum[xh_idx] - ((n - xh_idx) * nx))
    ans += left + right
    yl_idx = bisect_left(y_pos, ny)
    yh_idx = bisect_right(y_pos, ny)
    left = max(yl_idx * ny - y_sum[yl_idx], 0)
    right = max(0, y_sum[n] - y_sum[yh_idx] - ((n - yh_idx) * ny))
    ans += left + right
    x, y = nx, ny
    print(ans)
