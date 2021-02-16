# https://www.acmicpc.net/problem/1039
import sys
from itertools import combinations

read = sys.stdin.readline
n, k = read().strip().split()

k = int(k)
n = list(n)
dp = [[-1 for _ in range(1000001)] for _ in range(11)]

def getAns(d):
    global ans
    num = int("".join(n))
    if d == k:
        return num
    ret = -1
    if dp[d][num] != -1:
        return dp[d][num]
    for a, b in combinations(range(len(n)), 2):
        n[a], n[b] = n[b], n[a]
        if n[0] != '0':
            ret = max(ret, getAns(d + 1))
        n[a], n[b] = n[b], n[a]
    dp[d][num] = ret
    return ret

print(getAns(0))
