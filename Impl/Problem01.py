# https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque
def delsame(get,x):
    if len(get) < 1:
        return None
    if get[len(get) - 1] == x:
        get.pop()
        return 1
    return None   

def solution(board, moves):
    q = deque(map(deque,zip(*board)))    
    get = deque()
    cnt = 0
    for move in moves:
        if len(q[move-1]) == 0:
            continue
        x = q[move-1].popleft()
        while x == 0 and q[move-1]:
            x = q[move-1].popleft()
        if x != 0:
            if delsame(get,x) == 1:
                cnt += 1 
            else:
                get.append(x)
    return cnt *2;
 
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])