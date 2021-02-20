# https://www.acmicpc.net/problem/15684
import sys
from itertools import product, combinations

read = sys.stdin.readline
n, m, h = map(int, read().strip().split())
ans = list(range(1, n + 1))
ladders = [set() for _ in range(h)]
for _ in range(m):
    r, c = map(int, read().strip().split())
    ladders[r - 1].add(c)


def descend(arr, n_arr=[set() for _ in range(h)]):
    ret = list(range(n + 1))
    for i in range(h):
        for e in arr[i]:
            ret[e], ret[e + 1] = ret[e + 1], ret[e]
        for e in n_arr[i]:
            ret[e], ret[e + 1] = ret[e + 1], ret[e]
    return ret[1:]


tmp = list(product(range(h), range(1, n)))
for num in range(4):
    for e in combinations(tmp, num):
        flag = True
        n_arr = [set() for _ in range(h)]
        for r, c in e:
            if c in ladders[r] or (c - 1) in ladders[r] or (c + 1) in ladders[r]:
                flag = False
                break
            if (c+1) in n_arr[r] or (c - 1) in n_arr[r]:
                flag = False
                break
            n_arr[r].add(c)
        if flag and descend(ladders, n_arr) == ans:
            print(num)
            sys.exit()
print(-1)
