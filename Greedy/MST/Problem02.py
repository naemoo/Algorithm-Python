# https://www.acmicpc.net/problem/1944
import sys
from collections import deque

class UnionFind(object):
    class Node(object):
        def __init__(self, parent):
            self.parent = parent
            self.depth = 0

        def __repr__(self):
            return "({},{})".format(self.parent,self.depth)

    def find(self, i):
        if self.nodes[i].parent != i:
            self.nodes[i].parent = self.find(self.nodes[i].parent)
        return self.nodes[i].parent

    def merge(self, p, q):
        p, q = self.find(p), self.find(q)
        if self.nodes[p].depth == self.nodes[q].depth:
            self.nodes[p].depth += 1
            self.nodes[q].parent = p
        elif self.nodes[p].depth < self.nodes[q].depth:
            self.nodes[p].parent = q
        else:
            self.nodes[q].parent = p

    def __init__(self, n):
        self.n = n
        self.nodes = [self.Node(e) for e in range(n)]

    def __str__(self):
        return str(self.nodes)
inp = sys.stdin.readline
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
n, k = map(int, inp().strip().split())
graph, nodes = [], []
for i in range(n):
    graph.append([])
    for j, s in enumerate(inp().strip()):
        graph[i].append(s)
        if s == 'S' or s == 'K':
            nodes.append((i, j))
edges = []

def getDistance(start, end):
    visit = [[False] * n for _ in range(n)] 
    q = deque([(start[0], start[1], 0)])
    visit[start[0]][start[1]] = True

    while q:
        x, y, dp = q.popleft()
        for dx, dy in d:
            nx, ny, ndp = x+dx, y+dy, dp+1
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != '1' and (not visit[nx][ny]):
                q.append((nx, ny, ndp))
                visit[nx][ny] = True
                if end == (nx, ny):
                    return ndp
    return float('inf')


for i in range(len(nodes)):
    for j in range(len(nodes)):
        if j < i:
            edges.append((i,j,getDistance(nodes[i], nodes[j])))

u = UnionFind(len(nodes))
ans = 0
for p,q,w in sorted(edges,key= lambda x: x[2]):
    p,q = u.find(p),u.find(q)
    if p != q:
        u.merge(p,q)
        ans += w

print(ans if ans != float('inf') else -1)

