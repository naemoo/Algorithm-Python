# https://www.acmicpc.net/problem/2357
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())

arr = [0]

tree1 = [[float('inf'), 0] for _ in range(n + 1)]
tree2 = [[float('inf'), 0] for _ in range(n + 1)]

parentOf = lambda idx, bit1=True: idx + (idx & - idx) if bit1 else idx - (idx & - idx)


def add1(idx, num):
    while idx < len(tree1):
        tree1[idx][0] = min(tree1[idx][0], num)
        tree1[idx][1] = max(tree1[idx][1], num)
        idx = parentOf(idx)


def add2(idx, num):
    while idx > 0:
        tree2[idx][0] = min(tree2[idx][0], num)
        tree2[idx][1] = max(tree2[idx][1], num)
        idx = parentOf(idx, False)


for i in range(n):
    arr.append(int(read().strip()))
    add1(i + 1, arr[i + 1])
    add2(i + 1, arr[i + 1])


def getMinMax(a, b):
    ret1 = float('inf')
    ret2 = 0

    tmp = a
    while parentOf(tmp) <= b:
        ret1 = min(ret1, tree2[tmp][0])
        ret2 = max(ret2, tree2[tmp][1])
        tmp = parentOf(tmp)

    tmp = b
    while parentOf(tmp, False) >= a:
        ret1 = min(ret1, tree1[tmp][0])
        ret2 = max(ret2, tree1[tmp][1])
        tmp = parentOf(tmp, False)

    return min(ret1, arr[tmp]), max(ret2, arr[tmp])


for _ in range(m):
    a, b = map(int, read().strip().split())
    a, b = getMinMax(a, b)
    print(a, b)
