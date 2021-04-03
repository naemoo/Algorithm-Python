# https://www.acmicpc.net/problem/9372
import sys

read = sys.stdin.readline
test = int(read().strip())
while test:
    n, m = map(int, read().strip().split())
    while m:
        read().strip()
        m -= 1
    print(n - 1)
    test -= 1
