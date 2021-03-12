# https://www.acmicpc.net/problem/17611
import sys

read = sys.stdin.readline
n = int(read().strip())
points = []
for i in range(n):
    x, y = map(int, read().strip().split())
    points.append((x, y))

x_points = []
y_points = []

for i in range(n):
    p1, p2 = points[i], points[(i + 1) % n]
    if p1[1] == p2[1]:
        x_points.append((min(p1[0], p2[0]), 1))
        x_points.append((max(p1[0], p2[0]), -1))
    else:
        y_points.append((min(p1[1], p2[1]), 1))
        y_points.append((max(p1[1], p2[1]), -1))

x_points.sort()
y_points.sort()
x_max, x_cnt = 0, 0
y_max, y_cnt = 0, 0
for i in range(len(x_points)):
    x_cnt += x_points[i][1]
    x_max = max(x_cnt, x_max)
for i in range(len(y_points)):
    y_cnt += y_points[i][1]
    y_max = max(y_cnt, y_max)
print(max(x_max, y_max))
