# https://www.acmicpc.net/problem/1086
import sys
from math import gcd

read = sys.stdin.readline
n = int(read().strip())
nums = [read().strip() for _ in range(n)]
k = int(read().strip())

lens = list(map(len, nums))
mods = []
factorials = [1]
tens = [1]

for i in range(1, n + 1):
    factorials.append(factorials[-1] * i)
    mods.append(0)
    for j in range(lens[i - 1]):
        mods[-1] = (mods[-1] * 10 + int(nums[i - 1][j])) % k

for _ in range(51):
    tens.append((tens[-1] * 10) % k)
dp = [[-1 for _ in range(k)] for _ in range(1 << n)]
end = (1 << n) - 1



def dfs(state, mds):
    if state == end:
        return 1 if mds == 0 else 0

    if dp[state][mds] != -1:
        return dp[state][mds]

    ret = 0
    for i in range(n):
        if state & (1 << i) == 0:
            tmp = mds * tens[lens[i]] + mods[i]
            ret += dfs(state | (1 << i), tmp % k)
    dp[state][mds] = ret
    return ret


p, q = dfs(0, 0), factorials[n]
r = gcd(p, q)
print(p // r, q // r, sep='/')
