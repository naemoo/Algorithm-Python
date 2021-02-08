# https://www.acmicpc.net/problem/10714
import sys

sys.setrecursionlimit(2500)
read = sys.stdin.readline
n = int(read().strip())
cakes = [int(read().strip()) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def j_eat(l, r):
    if dp[l % n][r % n] != -1:
        return dp[l % n][r % n]

    if l == r:
        return cakes[l % n]
    ret = 0
    ret = i_eat(l + 1, r) + cakes[l % n]
    ret = max(i_eat(l, r - 1) + cakes[r % n], ret)
    dp[l % n][r % n] = ret
    return ret


def i_eat(l, r):
    if l == r:
        return 0
    ret = 0
    if cakes[l % n] > cakes[r % n]:
        ret = j_eat(l + 1, r)
    else:
        ret = j_eat(l, r - 1)
    return ret


ans = 0
for i in range(n):
    ans = max(ans, i_eat(i, n - 2 + i) + cakes[(i - 1 + n) % n])
print(ans)
