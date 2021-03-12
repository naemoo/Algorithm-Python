# https://www.acmicpc.net/problem/17070
import sys

read = sys.stdin.readline
n = int(read().strip())
house = [list(map(int, read().strip().split())) for _ in range(n)]

directions = {
    0: ((0, 0, 1, 0, 1), (2, 0, 1, 1, 1)), 1: ((1, 1, 0, 1, 0), (2, 1, 0, 1, 1)),
    2: ((0, 1, 1, 0, 1), (1, 1, 1, 1, 0), (2, 1, 1, 1, 1))}
conditions = {
    0: ([(0, 1)], ((0, 1), (1, 0), (1, 1))), 1: ([(1, 0)], ((1, 0), (1, 1), (0, 1))),
    2: ([(0, 1)], [(1, 0)], ((1, 0), (0, 1), (1, 1)))
}
dp = [[[[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(3)]
end = (n - 1, n - 1)


def go(state, l, r):
    if l == end or r == end:
        return 1
    if dp[state][l[0]][l[1]][r[0]][r[1]] != -1:
        return dp[state][l[0]][l[1]][r[0]][r[1]]

    ret = 0
    for condition, direction in zip(conditions[state], directions[state]):
        flag = True
        for con in condition:
            x, y = r
            dx, dy = con
            cx, cy = x + dx, y + dy
            if cx >= n or cy >= n or house[cx][cy] == 1:
                flag = False
        if flag:
            s, dx1, dy1, dx2, dy2 = direction
            ret += go(s, (l[0] + dx1, l[1] + dy1), (r[0] + dx2, r[1] + dy2))
    dp[state][l[0]][l[1]][r[0]][r[1]] = ret
    return ret


ans = go(0, (0, 0), (0, 1))
print(ans)
