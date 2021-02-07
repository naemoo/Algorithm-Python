# https://www.acmicpc.net/problem/1700
import sys
from collections import Counter

read = sys.stdin.readline
n, m = map(int, read().strip().split())
order = list(map(int, read().strip().split()))
cnt = Counter(order)
plugs = set()
zeros = set()
ans = 0

for i, e in enumerate(order):
    if len(plugs) < n:
        plugs.add(e)
    elif not e in plugs:
        if zeros:
            plugs.remove(zeros.pop())
            plugs.add(e)
        else:
            idx = 0
            for plug in plugs:
                for j in range(i + 1, len(order)):
                    if plug == order[j]:
                        idx = max(idx, j)
                        break
            plugs.remove(order[idx])
            plugs.add(e)
        ans += 1
        plugs.add(e)
    cnt[e] -= 1

    if cnt[e] == 0:
        zeros.add(e)

print(ans)
