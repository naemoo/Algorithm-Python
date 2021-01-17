# https://www.acmicpc.net/problem/1920
import sys

read = sys.stdin.readline
n = int(read().strip())
A = set(map(int, read().strip().split()))
m = int(read().strip())
ms = list(map(int, read().strip().split()))
for e in ms:
    if e in A:
        print(1)
    else:
        print(0)
