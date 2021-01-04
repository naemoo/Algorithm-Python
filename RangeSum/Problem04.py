# https://www.acmicpc.net/problem/2042
import sys

inp = sys.stdin.readline
n, m, k = map(int, inp().strip().split())

arr = []
for _ in range(n):
    arr.append(int(inp().strip()))


class BIT(object):
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    # idx 값 갱신
    def add(self, idx, num):
        idx += 1
        while idx < len(self.tree):
            self.tree[idx] += num
            idx += (idx & -idx)

    # [0:idx] 합
    def sum(self, idx):
        idx += 1
        ret = 0
        while idx > 0:
            ret += self.tree[idx]
            idx &= (idx - 1)
        return ret

    # [st:to] 합
    def sumRange(self, st, to):
        return self.sum(to) - self.sum(st - 1)


bit = BIT(n)
for i, e in enumerate(arr):
    bit.add(i, e)

for _ in range(k + m):
    a, b, c = map(int, inp().strip().split())

    if a == 1:
        bit.add(b - 1, c - arr[b - 1])
        arr[b - 1] = c
    else:
        print(bit.sumRange(b - 1, c - 1))
