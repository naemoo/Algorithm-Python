# https://www.acmicpc.net/problem/18235
import math
import sys

read = sys.stdin.readline
n, a, b = map(int, read().strip().split())
max_d = 21
duck = [[False for _ in range(500001)] for _ in (range(max_d))]
two_q = [1]
for _ in range(1, 21):
    two_q.append(two_q[-1] * 2)


def dfs(d, cur):
    if d == max_d:
        return
    duck[d][cur] = True
    if cur + two_q[d] <= n:
        dfs(d + 1, cur + two_q[d])
    if cur - two_q[d] > 0:
        dfs(d + 1, cur - two_q[d])


ans = float('inf')


def dfs2(d, cur):
    global ans
    if d == max_d:
        return

    if duck[d][cur]:
        ans = min(ans, d)
        return

    if cur + two_q[d] <= n:
        dfs2(d + 1, cur + two_q[d])
    if cur - two_q[d] > 0:
        dfs2(d + 1, cur - two_q[d])


dfs(0, a)
dfs2(0, b)
print(ans if ans != float('inf') else -1)
