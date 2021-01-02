# https://www.acmicpc.net/problem/11003
import sys

read = sys.stdin.readline
n, l = map(int, read().strip().split())
arr = [int(e) for e in read().strip().split()]
arr.insert(0, float('inf'))

tree1 = [float('inf')] * (n + 1)
tree2 = [float('inf')] * (n + 1)

parentOf = lambda i, bit1=True: i + (i & -i) if bit1 else i - (i & -i)


def update(idx, num):
    tmp = idx
    while tmp < len(tree1):
        tree1[tmp] = min(tree1[tmp], num)
        tmp += (tmp & -tmp)

    tmp = idx
    while tmp > 0:
        tree2[tmp] = min(tree2[tmp], num)
        tmp -= (tmp & -tmp)


def get(st, to):
    ret = float('inf')

    tmp = st
    while parentOf(tmp, True) <= to:
        ret = min(tree2[tmp], ret)
        tmp = parentOf(tmp, True)

    tmp = to
    while parentOf(tmp, False) >= st:
        ret = min(tree1[tmp], ret)
        tmp = parentOf(tmp, False)

    ret = min(ret, arr[tmp])
    return ret


for i in range(1, len(arr)):
    update(i, arr[i])

end = 1
for start in range(1, len(arr)):

    while end - start < l and end < len(arr):
        print(get(start,end),end=' ')
        end += 1

