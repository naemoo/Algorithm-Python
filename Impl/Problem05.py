#%% https://www.acmicpc.net/problem/1913
import sys
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, target = int(sys.stdin.readline()), int(sys.stdin.readline())
snail = [[0] * n for _ in range(n)]
cur,x,y = 0,0,0
answer = 0

for num in range(n**2,0,-1):
    if target == num:
        answer = x,y
    snail[x][y] = num
    nx,ny = x + d[cur][0], y+ d[cur][1]
    if 0<= nx < n and 0<= ny < n and snail[nx][ny] == 0:
        x,y = nx,ny
    else:
        cur = (cur + 1) % 4
        x,y = x + d[cur][0], y+ d[cur][1]
for s in snail:
    for e in s:
        print(e,end=' ')
    print()
print(answer[0] + 1,answer[1] + 1)

#%%
# %%
