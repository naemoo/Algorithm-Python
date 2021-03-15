# https://www.acmicpc.net/problem/2842
import sys
sys.setrecursionlimit(2501)
read = sys.stdin.readline
n = int(read().strip())
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
homes = []
altitude = []
s = set()
for i in range(n):
    for j, e in enumerate(read().strip()):
        if e == 'K':
            homes.append((i, j))
        elif e == 'P':
            post = (i, j)

for _ in range(n):
    e = list(map(int, read().strip().split()))
    s = s | set(tuple(e))
    altitude.append(e)
end = 0
fatigue = sorted(s)
ans = float('inf')


def canGo():
    for home in homes:
        x, y = home
        if not visit[x][y]:
            return False
    return True


def dfs(x, y):
    global low, high
    if x < 0 or y < 0 or n <= x or n <= y or altitude[x][y] < low or high < altitude[x][y] or visit[x][y]:
        return
    visit[x][y] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        dfs(nx, ny)


for i, start in enumerate(fatigue):
    visit = [[False for _ in range(n)] for _ in range(n)]
    while end < len(fatigue):
        visit = [[False for _ in range(n)] for _ in range(n)]
        low, high = start, fatigue[end]
        dfs(post[0], post[1])
        if canGo():
            ans = min(ans, high - low)
            break
        end += 1

print(ans)