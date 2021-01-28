# https://www.acmicpc.net/problem/10868
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = [0]
for _ in range(n):
    arr.append(int(read().strip()))

tree1 = [float('inf') for _ in range(n + 1)]
tree2 = [float('inf') for _ in range(n + 1)]


def update(idx, e):
    i = idx
    while i > 0:
        tree2[i] = min(tree2[i], e)
        i -= (i & -i)
    i = idx
    while i <= n:
        tree1[i] = min(tree1[i], e)
        i += (i & -i)


def getMin(a, b):
    ret = float('inf')
    cur = a
    while cur + (cur & -cur) <= b:
        ret = min(tree2[cur], ret)
        cur += (cur & -cur)
    cur = b
    while cur - (cur & -cur) >= a:
        ret = min(tree1[cur], ret)
        cur -= (cur & -cur)
    ret = min(ret, arr[cur])
    return ret


for i, e in enumerate(arr):
    if i:
        update(i, e)

while m:
    a, b = map(int, read().strip().split())
    print(getMin(a, b))
    m -= 1
