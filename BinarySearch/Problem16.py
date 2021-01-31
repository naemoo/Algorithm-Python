# https://www.acmicpc.net/problem/1072
import sys

read = sys.stdin.readline
x, y = map(int, read().strip().split())
org = (y * 100 // x)

if org >= 99:
    print(-1)
    sys.exit()

l, r = 0, 1000000000

while l < r:
    mid = (l + r) // 2
    tmp = int(((y + mid) * 100 // (x + mid)))

    if tmp <= org:
        l = mid + 1
    else:
        r = mid

print(r)
