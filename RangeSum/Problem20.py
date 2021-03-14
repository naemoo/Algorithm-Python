# https://www.acmicpc.net/problem/2616
import sys

sys.setrecursionlimit(50005)
read = sys.stdin.readline
n = int(read().strip())
trains = list(map(int, read().strip().split()))
prefix = [0]
dp = [[-1 for _ in range(50005)] for _ in range(3)]
k = int(read().strip())
for train in trains:
    prefix.append(prefix[-1] + train)


def go(d, start):
    if d == 3:
        return 0
    if start > n:
        return -float('inf')

    if dp[d][start] != -1:
        return dp[d][start]

    ret = max(go(d, start + 1), go(d + 1, start + k) + prefix[start] - prefix[start - k])
    dp[d][start] = ret
    return ret


print(go(0, k))
