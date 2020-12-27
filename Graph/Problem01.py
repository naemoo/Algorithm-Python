# https://www.acmicpc.net/problem/10451
import sys

read = sys.stdin.readline
t = int(read().strip())


def find(arr, n):
    if arr[n][0] == n:
        return n
    arr[n][0] = find(arr, arr[n][0])
    return arr[n][0]


def merge(arr, p, q):
    p, q = find(arr, p), find(arr, q)

    if arr[p][1] < arr[q][1]:
        arr[p][0] = q
    elif arr[p][1] > arr[q][1]:
        arr[q][0] = p
    else:
        arr[q][1] += 1
        arr[p][0] = q


for _ in range(t):
    n = int(read().strip())
    arr = [int(e) for e in read().strip().split()]
    nodes = [[i, 0] for i in range(n + 1)]
    for i, e in enumerate(arr):
        i += 1
        p, q = find(nodes, i), find(nodes, e)
        if p != q:
            merge(nodes, p, q)

    ans = set()

    for e in arr:
        ans.add(find(nodes,e))
    print(len(ans))
