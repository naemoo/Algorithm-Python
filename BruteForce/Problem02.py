# https://www.acmicpc.net/problem/4991
import sys
from collections import deque
from itertools import permutations

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
inp = sys.stdin.readline

cmd = inp().strip()


def getShortestPath(graph, dest, start):
    if dest == start:
        return 0

    visit = [([True] * len(graph[0])) for _ in range(len(graph))]
    x, y = start
    visit[x][y] = False
    q = deque()
    q.append([x, y, 0])

    while q:
        x, y, w = q.popleft()

        for dx, dy in d:
            nx, ny, nw = dx + x, dy + y, w + 1

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if visit[nx][ny] and graph[nx][ny] != 'x':
                    visit[nx][ny] = False
                    q.append((nx, ny, nw))
                if (nx, ny) == dest:
                    return nw
    return float('inf')


while cmd != '0 0':
    x, y = map(int, cmd.split())
    graph = [[e for e in inp().strip()] for _ in range(y)]
    dirties = deque()

    for i in range(y):
        for j in range(x):
            if graph[i][j] == 'o':
                dirties.appendleft((i, j))
            elif graph[i][j] == '*':
                dirties.append((i, j))


    edges = [[0] * len(dirties) for _ in range(len(dirties))]
    for i in range(len(edges)):
        for j in range(len(edges)):
            if i < j:
                edges[i][j] = getShortestPath(graph, dirties[i], dirties[j])
                edges[j][i] = edges[i][j]

    ans = float('inf')
    for seq in permutations(range(1, len(dirties)), len(dirties) - 1):
        s = edges[0][seq[0]]
        for i in range(len(seq) - 1):
            s += edges[seq[i]][seq[i + 1]]
        ans = min(ans, s)
    print(ans if ans != float('inf') else -1)
    cmd = inp().strip()
