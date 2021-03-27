# https://www.acmicpc.net/problem/10800
import sys
from bisect import bisect_left
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
marbles = [tuple(map(int, read().strip().split())) for _ in range(n)]
sorted_marbles = sorted(marbles, key=lambda x: x[1])
all_pre = [0 for _ in range(n + 1)]
kind_marble = defaultdict(list)
kind_pre = defaultdict(list)
for i in range(1, n + 1):
    kind, kind_size = sorted_marbles[i - 1]
    all_pre[i] = all_pre[i - 1] + kind_size
    kind_marble[kind].append(kind_size)
    if len(kind_pre[kind]) == 0:
        kind_pre[kind].append(0)
    kind_pre[kind].append(kind_pre[kind][-1] + kind_size)
sorted_marbles = list(map(lambda x: x[1], sorted_marbles))
for k, s in marbles:
    idx = bisect_left(sorted_marbles, s)
    k_idx = bisect_left(kind_marble[k], s)
    total = all_pre[idx] - kind_pre[k][k_idx]
    print(total)
