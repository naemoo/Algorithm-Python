# https://www.acmicpc.net/problem/3078
import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, read().strip().split())
friends = [read().strip() for _ in range(n)]
q = deque()
relationship = [0 for _ in range(21)]
ans = 0

for friend in friends:
    relationship[len(friend)] += 1
    q.append(friend)

    if relationship[len(friend)] > 1:
        ans += relationship[len(friend)] - 1

    if len(q) > k:
        popleft = q.popleft()
        relationship[len(popleft)] -= 1

print(ans)
