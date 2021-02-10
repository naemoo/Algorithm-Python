# https://www.acmicpc.net/problem/11066
import sys

read = sys.stdin.readline

t = int(read().strip())


def file_merge(start, end):
    if dp[start][end] != -1:
        return dp[start][end]

    if start == end:
        return 0
    tmp = prefix[end + 1] - prefix[start]
    ret = float('inf')
    for k in range(start, end):
        ret = min(ret, file_merge(start, k) + file_merge(k + 1, end) + tmp)
    dp[start][end] = ret
    return ret


while t:
    n = int(read().strip())
    files = list(map(int, read().strip().split()))
    prefix = [0]
    e = 0
    for file in files:
        e += file
        prefix.append(e)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    print(file_merge(0, n - 1))
    t -= 1
