# https://www.acmicpc.net/problem/1107
import sys

read = sys.stdin.readline
n = int(read().strip())
read().strip()
btns = [e for e in read().strip().split()]
btns = set(btns)
ret = abs(n - 100)

for x in range(1000000):
    strX = str(x)
    if len(set(strX) & btns) == 0:
        ret = min(ret, abs(n - x) + len(strX))
print(ret)
