# https://programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
d = ((1, 0, 'v'), (-1, 0, 'v'), (0, 1, 'h'), (0, -1, 'h'))

def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 0, 0, 'h'))
    q.append((0, 0, 0, 'v'))
    visit = [[float('inf')] * n for _ in range(n)]
    visit[0][0] = 0

    while q:
        cost, x, y, stat = q.popleft()

        for dx, dy, ns in d:
            nx, ny = x+dx, y+dy
            ncost = cost + 100 + (500 if ns != stat else 0)

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if visit[nx][ny] >= ncost:
                    q.append((ncost, nx, ny, ns))
                    visit[nx][ny] = ncost

    print(visit[n-1][n-1])

solution([[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
