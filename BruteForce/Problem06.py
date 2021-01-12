# https://www.acmicpc.net/problem/18119
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
words = []
forget = 0

for _ in range(n):
    word = 0
    for w in read().strip():
        c = ord(w) - ord('a')
        word |= 1 << c
    words.append(word)

for _ in range(m):
    cmd, c = read().strip().split()
    c = ord(c) - ord('a')
    if cmd == '1':
        forget |= (1 << c)
    else:
        if forget & (1 << c) != 0:
            forget ^= (1 << c)

    cnt = n
    for word in words:
        if word & forget != 0:
            cnt -= 1
    print(cnt)
