# https://www.acmicpc.net/problem/1717
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
union = [[i, 1] for i in range(n + 1)]


def find(idx):
    if union[idx][0] == idx:
        return idx
    union[idx][0] = find(union[idx][0])
    return union[idx][0]


def merge(p, q):
    p, q = find(p), find(q)
    if union[p][1] > union[q][1]:
        union[q][0] = p
    elif union[p][1] < union[q][1]:
        union[p][0] = q
    else:
        union[q][0] = p
        union[p][1] += 1


while m:
    c, a, b = map(int, read().strip().split())
    if c:
        a, b = find(a), find(b)
        if a == b:
            print("YES")
        else:
            print("NO")
    else:
        merge(a, b)
    m -= 1
