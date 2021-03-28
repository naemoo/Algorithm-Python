# https://www.acmicpc.net/problem/9997
import sys

read = sys.stdin.readline
n = int(read().strip())
words = [read().strip() for _ in range(n)]
alpha = [0] * n

for i, word in enumerate(words):
    for c in word:
        alpha[i] |= 1 << (ord(c) - ord('a'))

flag = (1 << 26) - 1
ans = 0


def go(d, tmp):
    global ans
    if d == n:
        if tmp == flag:
            ans += 1
        return

    go(d + 1, tmp | alpha[d])
    go(d + 1, tmp)


go(0, 0)
print(ans)
