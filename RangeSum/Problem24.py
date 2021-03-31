# https://www.acmicpc.net/problem/2015
import sys
from collections import Counter

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

ans = 0
count = Counter()

for e in prefix[1:]:
    if e == m:
        ans += 1
    ans += count[e - m]
    count[e] += 1

print(ans)
