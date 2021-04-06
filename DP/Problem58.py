# https://www.acmicpc.net/problem/1176
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
students = [int(read().strip()) for _ in range(n)]
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]


def punish(cur, state):
    if state == (1 << n) - 1:
        return 1
    if dp[cur][state] != -1:
        return dp[cur][state]

    ret = 0
    for i in range(n):
        if state & (1 << i) == 0 and abs(students[cur] - students[i]) > k:
            ret += punish(i, state | (1 << i))
    dp[cur][state] = ret
    return ret


ans = 0
for i, student in enumerate(students):
    ans += punish(i, 1 << i)
print(ans)
