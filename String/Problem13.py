# https://www.acmicpc.net/problem/16719
import sys
from bisect import insort_left

read = sys.stdin.readline
word = read().strip()
n = len(word)
visit = [False for _ in range(n)]
ans = []


def go(l, r):
    global ans
    if l > r:
        return
    for i, e, in sorted(enumerate(word[l:r + 1], start=l), key=lambda x: x[1]):
        if visit[i]:
            continue
        visit[i] = True
        insort_left(ans, (i, e))
        print(''.join(map(lambda x: x[1], ans)))
        go(i + 1, r)


go(0, n - 1)
