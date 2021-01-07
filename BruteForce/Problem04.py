# https://www.acmicpc.net/problem/10836
import sys

read = sys.stdin.readline
m, n = map(int, read().strip().split())

house = [[1 for _ in range(m)] for _ in range(m)]

for _ in range(n):
    a, b, c = map(int, read().strip().split())
    idx = -m + 1

    for i in range(idx + a, idx + a + b):
        if i <= 0:
            house[abs(i)][0] += 1
        else:
            house[0][i] += 1
    for i in range(idx + a + b, m):
        if i <= 0:
            house[abs(i)][0] += 2
        else:
            house[0][i] += 2

for i in range(1, m):
    for j in range(1, m):
        house[i][j] = house[i - 1][j]

for arr in house:
    for e in arr:
        print(e, end=' ')
    print()
