# https://www.acmicpc.net/problem/17071
import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, read().strip().split())
max_range = 500000
visit = [[-1 for _ in range(max_range + 1)] for _ in range(2)]
directions = (0, 1, -1)
q = deque()
q.append((n, 0, k))
visit[0][n] = 0

while q:
    s_pos, time, b_pos = q.popleft()
    if visit[time % 2][b_pos] != -1 and visit[time % 2][b_pos] <= time:
        print(time)
        sys.exit()

    for direction in directions:
        nxt_spos = s_pos + direction if direction else s_pos * 2
        nxt_time = time + 1
        nxt_bpos = nxt_time + b_pos

        if nxt_spos < 0 or nxt_spos > max_range or nxt_bpos > max_range or visit[nxt_time % 2][nxt_spos] != -1:
            continue
        q.append((nxt_spos, nxt_time, nxt_bpos))
        visit[nxt_time % 2][nxt_spos] = nxt_time

print(-1)
