# https://www.acmicpc.net/problem/14719
import sys

read = sys.stdin.readline
h, w = map(int, read().strip().split())
blocks = [int(e) for e in read().strip().split()]
s = []

arr1 = [0] * len(blocks)
for i in range(w):
    while s and s[-1][0] <= blocks[i]:
        x, y = s.pop()
        arr1[y] = (blocks[i], i)
    s.append((blocks[i], i))

arr2 = [0] * len(blocks)
s = []
for i in range(w - 1, -1, -1):
    while s and s[-1][0] <= blocks[i]:
        x, y = s.pop()
        arr2[y] = (blocks[i], i)
    s.append((blocks[i], i))

visit = [True] * (len(blocks))
ret = 0
l, r = 0, len(arr2) - 1
visit[l] = visit[r] = False
while l < len(arr1):
    if arr1[l] == 0:
        break
    nxt = arr1[l][1]
    e = blocks[l]

    while l < nxt:
        if visit[l]:
            ret += e - blocks[l]
            visit[l] = False
        l += 1

while r >= 0:
    if arr2[r] == 0:
        break
    nxt = arr2[r][1]
    e = blocks[r]

    while r > nxt:
        if visit[r]:
            ret += e - blocks[r]
            visit[r] = False
        r -= 1
print(ret)
