# https://www.acmicpc.net/problem/1062
import sys

sys.setrecursionlimit(100)

read = sys.stdin.readline
n, k = map(int, read().strip().split())
words = [read().strip() for _ in range(n)]
learn = {'a', 'n', 't', 'i', 'c'}
ret = 0


def dfs(start, d):
    global ret
    if d == k - 5:
        cnt = 0
        for word in words:
            for i, w in enumerate(word):
                if not w in learn:
                    break
                if i == len(word) - 1:
                    cnt += 1
        ret = max(ret, cnt)
        return

    for e in range(start, ord('z') + 1):
        if not chr(e) in learn:
            learn.add(chr(e))
            dfs(e + 1, d + 1)
            learn.remove(chr(e))
if k >= 5:
    dfs(ord('a'), 0)
    print(ret)
else:
    print(0)

