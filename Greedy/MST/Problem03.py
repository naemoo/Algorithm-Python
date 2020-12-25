# https://www.acmicpc.net/problem/1922
import sys
from collections import defaultdict

inp = sys.stdin.readline
n = int(inp().strip())
tree = defaultdict(lambda: defaultdict(lambda: float('inf')))
edges = []

for _ in range(int(inp().strip())):
    st, to, w = map(int, inp().strip().split())
    edges.append((w, st - 1, to - 1))
edges.sort()


class Node(object):
    def __init__(self, i):
        self.parent = i
        self.depth = 0

    def __repr__(self):
        return str(self.parent)


arr = [Node(i) for i in range(n)]


def find(i):
    if arr[i].parent == i:
        return i
    arr[i].parent = find((arr[i]).parent)
    return arr[i].parent


def merge(p, q):
    p, q = find(p), find(q)
    if arr[p].depth < arr[q].depth:
        arr[p].parent = q
    elif arr[p].depth > arr[q].depth:
        arr[q].parent = p
    else:
        arr[p].depth += 1
        arr[q].parent = p


ans = 0
for w, p, q in edges:
    p, q = find(p), find(q)
    if p != q:
        merge(p, q)
        ans += w
print(ans)
