# https://programmers.co.kr/learn/courses/30/lessons/67259
import heapq
d = ((1, 0, 'v'), (-1, 0, 'v'), (0, 1, 'h'), (0, -1, 'h'))
def solution(board):
    n = len(board)
    visit = {'h' : [[float('inf')] * len(board) for _ in range(len(board))],
           'v' : [[float('inf')] * len(board) for _ in range(len(board))]}    
    q = [(0,0,0,'h'),(0,0,0,'v')]
    visit['h'][0][0] = 0
    visit['v'][0][0] = 0
    
    while q:
        cost,x,y,s = heapq.heappop(q)
        
        if visit[s][x][y] < cost:
            continue
        for dx,dy,ns in d:
            nx, ny = x + dx, y + dy
            ncost = cost + (600 if ns != s else 100)
            if 0 <= nx < n and 0<= ny < n and board[nx][ny] == 0:
                if ncost < visit[ns][nx][ny]:
                    heapq.heappush(q,(ncost,nx,ny,ns))
                    visit[ns][nx][ny] = ncost
    return min(visit['v'][n-1][n-1],visit['h'][n-1][n-1])    