# https://www.acmicpc.net/problem/17472
import sys
from collections import deque, defaultdict

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
read = sys.stdin.readline
n, m = map(int, read().strip().split())
islands = [list(map(int, read().strip().split())) for _ in range(n)]

v = 0
visit = [[0 for _ in range(m)] for _ in range(n)]
locations = defaultdict(list)
for a in range(n):
    for j in range(m):
        if islands[a][j] and not visit[a][j]:
            visit[a][j] = v + 1
            locations[visit[a][j]].append((a, j))
            q = deque([(a, j)])
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] != 0:
                        continue
                    if islands[a][j] != islands[nx][ny]:
                        continue
                    q.append((nx, ny))
                    visit[nx][ny] = v + 1
                    locations[visit[nx][ny]].append((nx, ny))
            v += 1

islands = visit
bridges = []


def getEdge(island, x, y):
    ret = []
    for dx, dy in directions:
        nx, ny, d = x, y, 0
        while True:
            nx, ny = nx + dx, ny + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if islands[nx][ny]:
                if island == islands[nx][ny] or d == 1:
                    break
                ret.append((islands[nx][ny], d))
                break
            d += 1
    return ret


for a in range(1, v + 1):
    for x, y in locations[a]:
        for b, c in getEdge(a, x, y):
            bridges.append((c, a, b))
bridges.sort()
ans = 0
tree = [i for i in range(v + 1)]


def find(idx):
    if idx == tree[idx]:
        return idx
    tree[idx] = find(tree[idx])
    return tree[idx]


def merge(a, b):
    a, b = find(a), find(b)
    tree[b] = a

cnt = 0
for c, a, b in bridges:
    if find(a) != find(b):
        merge(a, b)
        ans += c
        cnt += 1

print(ans if cnt == v - 1 else -1)
