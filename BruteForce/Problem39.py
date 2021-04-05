# https://www.acmicpc.net/problem/11578
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
friends = []
all_sol = (1 << n) - 1
for _ in range(m):
    tmp = 0
    for e in map(int, read().strip().split()[1:]):
        tmp |= 1 << (e - 1)
    friends.append(tmp)

ans = float('inf')
for i in range(1 << m):
    tmp = 0
    cnt = 0
    for j in range(m):
        if i & (1 << j):
            cnt += 1
            tmp |= (friends[j])

    if tmp == all_sol:
        ans = min(ans, cnt)
print(ans if ans != float('inf') else -1)
