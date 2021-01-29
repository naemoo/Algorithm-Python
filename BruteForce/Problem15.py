# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

read = sys.stdin.readline
n, m = map(int, read().strip().split())

# 거리 |r1 - r2| + |c1 - c2|,  도시 치킨 거리 = 모든집의 치킨거리

cities = [list(map(int, read().strip().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        e = cities[i][j]
        if e == 2:
            chickens.append((i, j))
        elif e == 1:
            houses.append((i, j))

ret = float('inf')
for notClose in combinations(chickens, m):
    distance = 0
    for house in houses:
        tmp = float('inf')
        for chicken in notClose:
            tmp = min(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]), tmp)
        distance += tmp
    ret = min(ret, distance)

print(ret)
