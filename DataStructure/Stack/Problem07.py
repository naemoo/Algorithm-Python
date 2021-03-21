# https://www.acmicpc.net/problem/3015
import sys

read = sys.stdin.readline
n = int(read().strip())
height = [int(read().strip()) for _ in range(n)]
cnt = [1 for _ in range(n)]
s = []
ans = 0

for i, e in enumerate(height):
    while s:
        if s[-1][1] <= e:
            idx, h = s.pop()
            ans += cnt[idx]
            if h == e:
                cnt[i] += cnt[idx]
        else:
            ans += 1
            break
    s.append((i, e))
print(ans)
