# https://www.acmicpc.net/problem/3955
import sys
from math import gcd

read = sys.stdin.readline


def eGcd(a, b):
    s0, t0, r0 = 1, 0, a
    s1, t1, r1 = 0, 1, b

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, (r0 - r1 * q)
        s0, s1 = s1, (s0 - s1 * q)
        t0, t1 = t1, (t0 - t1 * q)
    return s0, t0, r0


t = int(read().strip())
while t:
    k, c = map(int, read().strip().split())
    if k == 1 or c == 1:
        if k == 1 and c == 1:
            print(2)
        elif c == 1:
            if k + 1 > 10 ** 9:
                print("IMPOSSIBLE")
            else:
                print(k + 1)
        elif k == 1:
            print(1)
        t -= 1
        continue
    elif gcd(k, c) != 1:
        t -= 1
        print("IMPOSSIBLE")
        continue
    ans = eGcd(k, c)[1]
    print(ans if ans >= 0 else k + ans)
    t -= 1
