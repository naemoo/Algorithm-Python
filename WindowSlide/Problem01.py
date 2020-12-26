# https://www.acmicpc.net/problem/11003
import sys
from collections import deque

inp = sys.stdin.readline
n, l = map(int, inp().strip().split())
arr = [int(e) for e in map(int, inp().strip().split())]

q = deque()

for i,e in enumerate(arr):

    while q and q[len(q) - 1][0] > e:
        q.pop()

    q.append((e,i))

    while q and q[0][1] < i - l + 1:
        q.popleft()

    print(q[0][0],end=' ')