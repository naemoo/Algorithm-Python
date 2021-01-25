# https://www.acmicpc.net/problem/2252
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
n, m = map(int, read().strip().split())
students = defaultdict(list)
indegrees = [0 for _ in range(n + 1)]

while m:
    a, b = map(int, read().strip().split())
    students[a].append(b)
    indegrees[b] += 1
    m -= 1

q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    e = q.popleft()
    print(e, end=' ')
    for student in students[e]:
        indegrees[student] -= 1
        if not indegrees[student]:
            q.append(student)
