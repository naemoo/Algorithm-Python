# https://www.acmicpc.net/problem/2056
import sys

read = sys.stdin.readline
n = int(read().strip())
times = [0 for _ in range(n + 1)]
ans = 0

for i in range(1, n + 1):
    tmp = list(map(int, read().strip().split()))
    spend_time, pre = tmp[0], tmp[2:]
    pre_time = 0
    for idx in pre:
        pre_time = max(pre_time, times[idx])
    times[i] = pre_time + spend_time
    ans = max(ans, times[i])

print(ans)
