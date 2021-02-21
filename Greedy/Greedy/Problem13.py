# https://www.acmicpc.net/problem/17619
import sys
from itertools import chain
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 5 + 2)
read = sys.stdin.readline
n, q = map(int, read().strip().split())
trees = [tuple(chain(map(int, read().strip().split()), [i + 1])) for i in range(n)]
trees.sort(key=lambda x: (x[1], x[0]))
union = [[i, 0] for i in range(n + 1)]


def find(idx):
    if union[idx][0] == idx:
        return idx
    union[idx][0] = find(union[idx][0])
    return union[idx][0]


def merge(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if union[a][1] < union[b][1]:
        union[a][0] = b
    elif union[a][1] > union[b][1]:
        union[b][0] = a
    else:
        union[a][0] = b
        union[b][1] += 1


hq = []
for tree in trees:
    while hq and -hq[0][0] >= tree[0]:
        a, b = heappop(hq)
        merge(b, tree[3])
    heappush(hq, (-tree[1], tree[3]))
while q:
    a, b = map(int, read().strip().split())
    a, b = find(a), find(b)
    if a != b:
        print(0)
    else:
        print(1)
    q -= 1
