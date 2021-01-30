# https://www.acmicpc.net/problem/19942
import sys
from collections import defaultdict
from itertools import combinations

read = sys.stdin.readline
n = int(read().strip())
mp, mf, ms, mv = map(int, read().strip().split())
gradients = [list(map(int, read().strip().split())) for _ in range(n)]

cost = float('inf')
ans = defaultdict(list)
for i in range(1, n + 1):
    for com in combinations(enumerate(gradients), i):
        tmp = []
        sum_p, sum_f, sum_s, sum_v, sum_c = 0, 0, 0, 0, 0
        for e in com:
            p, f, s, v, c = e[1]
            sum_p += p
            sum_f += f
            sum_s += s
            sum_v += v
            sum_c += c
            tmp.append(e[0] + 1)
        if sum_p >= mp and sum_v >= mv and sum_f >= mf and sum_s >= ms:
            if cost >= sum_c:
                cost = sum_c
                ans[cost].append(tuple(tmp))

if cost == float('inf'):
    print(-1)
else:
    print(cost)
    for e in sorted(ans[cost])[0]:
        print(e, end=' ')
