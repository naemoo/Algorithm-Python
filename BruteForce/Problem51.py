# https://www.acmicpc.net/problem/7573
import sys

read = sys.stdin.readline
n, l, m = map(int, read().strip().split())
fish = []

for _ in range(m):
    fish.append(tuple(map(int, read().strip().split())))

ans = 0
for x in range(1, l // 2):
    y = (l // 2) - x
    for i1, j1 in fish:
        for i2, j2 in fish:
            tmp = 0
            for i, j in fish:
                if i1 <= i <= i1 + x and j2 <= j <= j2 + y:
                    tmp += 1
            ans = max(tmp, ans)
print(ans)
