# https://www.acmicpc.net/problem/9576
import sys

read = sys.stdin.readline
t = int(read().strip())

for _ in range(t):
    n, m = map(int, read().strip().split())
    ms = []
    for _ in range(m):
        a, b = map(int, read().strip().split())
        ms.append((a, b))

    ms = sorted(ms, key=lambda x: x[1])
    idx, ret = 0, 0
    visit = [True] * (n + 1)

    for a, b in ms:
        for i in range(a, b + 1):
            if visit[i]:
                ret += 1
                visit[i] = False
                break
    print(ret)
