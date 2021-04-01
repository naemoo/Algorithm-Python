# https://www.acmicpc.net/problem/10986
import sys
from collections import Counter

read = sys.stdin.readline
n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
prefix = [0]
prev = Counter()

for e in arr:
    prefix.append(prefix[-1] + e)

ans = 0
for e in prefix[1:]:
    if e % m == 0:
        ans += 1
    ans += prev[e % m]
    prev[e % m] += 1
print(ans)