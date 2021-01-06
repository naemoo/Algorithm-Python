# https://www.acmicpc.net/problem/2493
import sys

read = sys.stdin.readline
n = int(read())
towers = [int(tower) for tower in read().strip().split()]
towers.reverse()

stack = []
ans = [0] * n

for i, e in enumerate(towers):
    while stack and stack[-1][1] <= e:
        x, y = stack.pop()
        ans[n - 1 - x] = n - i
    stack.append((i, e))
for e in ans:
    print(e,end=' ')