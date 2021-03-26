# https://www.acmicpc.net/problem/1285
import sys

read = sys.stdin.readline
n = int(read().strip())
coins = [list(map(lambda x: 0 if x == 'H' else 1, read().strip())) for _ in range(n)]
ans = float('inf')
for k in range(1 << n):
    total = 0
    for j in range(n):
        tmp = 0
        for i in range(n):
            e = coins[i][j]
            if k & (1 << i):
                e = 0 if e else 1
            if e:
                tmp += 1
        total += min(tmp, n - tmp)
    ans = min(ans,total)

print(ans)
