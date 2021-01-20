# https://www.acmicpc.net/problem/17822
import sys
from collections import deque

read = sys.stdin.readline
n, m, t = map(int, read().strip().split())
plates = [deque(map(int, read().strip().split())) for _ in range(n)]


def rotate(arr, d, k):
    while k:
        if d:
            arr.append(arr.popleft())
        else:
            arr.appendleft(arr.pop())
        k -= 1


while t:
    x, d, k = map(int, read().strip().split())
    for i in range(x, n + 1, x):
        rotate(plates[i - 1], d, k)

    check = [[False] * (m) for _ in range(n)]

    for i in range(n):
        u, d = max(0, i - 1), min(i + 1, n - 1)
        for j in range(m):
            l, r = (j - 1 + m) % m, (j + 1) % m
            isSame = False
            if plates[i][j] == 0:
                continue

            if u != i and plates[i][j] == plates[u][j]:
                check[u][j] = True
                isSame = True
            if d != i and plates[i][j] == plates[d][j]:
                check[d][j] = True
                isSame = True

            if plates[i][j] == plates[i][l]:
                check[i][l] = True
                isSame = True

            if plates[i][j] == plates[i][r]:
                check[i][r] = True
                isSame = True

            if isSame:
                check[i][j] = True

    flag = True
    for i in range(n):
        for j in range(m):
            if check[i][j]:
                plates[i][j] = 0
                flag = False

    if flag:
        avg = 0
        cnt = 0
        for plate in plates:
            for e in plate:
                if e > 0:
                    cnt += 1
                    avg += e
        if cnt == 0:
            t -= 1
            continue

        avg = avg / cnt
        for plate in plates:
            for i, e in enumerate(plate):
                if e < avg and e != 0:
                    plate[i] += 1
                elif e > avg and e != 0:
                    plate[i] -= 1

    t -= 1

ans = 0
for plate in plates:
    ans += sum(plate)
print(ans)
