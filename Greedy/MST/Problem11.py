# https://programmers.co.kr/learn/courses/30/lessons/62050
from collections import deque, defaultdict

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def solution(land, height):
    n = len(land)
    arr = [[-1 for _ in range(n)] for _ in range(n)]
    cnt = 0

    def bfs(cur, area):
        q = deque()
        q.append(cur)
        arr[cur[0]][cur[1]] = area

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != -1:
                    continue

                if abs(land[x][y] - land[nx][ny]) > height:
                    continue

                arr[nx][ny] = area
                q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                bfs((i, j), cnt)
                cnt += 1

    adj = defaultdict(lambda: defaultdict(lambda: float('inf')))

    for x in range(n):
        for y in range(n):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == arr[x][y]:
                    continue
                u, v = arr[x][y], arr[nx][ny]

                adj[u][v] = min(adj[u][v], abs(land[nx][ny] - land[x][y]))
                adj[v][u] = min(adj[v][u], abs(land[nx][ny] - land[x][y]))

    edges = []
    for k in adj:
        for v, w in adj[k].items():
            edges.append((k, v, w))
    edges.sort(key=lambda x: x[2])

    tree = [[i, 1] for i in range(cnt)]

    def find(idx):
        if idx == tree[idx][0]:
            return idx

        tree[idx][0] = find(tree[idx][0])
        return tree[idx][0]

    def merge(p, q):
        if tree[p][1] < tree[q][1]:
            tree[p][0] = q
            tree[q][1] += tree[p][1]
        else:
            tree[q][0] = p
            tree[p][1] += tree[q][1]

    ans = 0
    for a, b, w in edges:
        a, b = find(a), find(b)
        if a != b:
            ans += w
            merge(a, b)
    return ans
