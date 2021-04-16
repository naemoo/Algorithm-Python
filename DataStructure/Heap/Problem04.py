# https://www.acmicpc.net/problem/1379
import sys
from collections import deque

read = sys.stdin.readline
n = int(read().strip())
classes = []
for _ in range(n):
    class_num, start, end = map(int, read().strip().split())
    classes.append((start, 1, class_num))
    classes.append((end, -1, class_num))

classes.sort()
ans = 0
tmp = 0
ans_class = {}
for time, v, num in classes:
    tmp += v
    ans = max(ans, tmp)

q = deque(range(1, ans + 1))
for time, v, num in classes:
    if v > 0:
        ans_class[num] = q.popleft()
    else:
        q.append(ans_class[num])

print(ans)
for i in range(1, n + 1):
    print(ans_class[i])
