# https://www.acmicpc.net/problem/3830
import sys
sys.setrecursionlimit(10**5+5)
read = sys.stdin.readline
n, m = map(int, read().strip().split())

def find(idx):
    if tree[idx][0] == idx:
        return idx, 0
    ret = tree[idx][1]
    tmp = find(tree[idx][0])
    ret += tmp[1]

    tree[idx][0] = tmp[0]
    tree[idx][1] = ret
    return tree[idx][0], ret


def merge(a, b, w):
    a, aw = find(a)
    b, bw = find(b)
    bw += w
    if aw > bw:
        tree[b][0] = a
        tree[b][1] = aw - bw
    else:
        tree[a][0] = b
        tree[a][1] = bw - aw


while n and m:
    tree = [[i, 0] for i in range(n + 1)]
    for _ in range(m):
        tmp = read().strip().split()
        if tmp[0] == '!':
            a, b, c = map(int, tmp[1:])
            merge(a, b, c)
        elif tmp[0] == '?':
            a, b = map(int, tmp[1:])
            a, b = find(a), find(b)
            if a[0] != b[0]:
                print('UNKNOWN')
            else:
                print(a[1] - b[1])
    n, m = map(int, read().strip().split())
