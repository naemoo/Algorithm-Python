# https://www.acmicpc.net/problem/1735
import sys
from math import gcd

read = sys.stdin.readline
a, b = map(int, read().strip().split())
c, d = map(int, read().strip().split())

gc = gcd(b, d)
lcm = gc * (b // gc) * (d // gc)

ans1 = a * (lcm // b) + c * (lcm // d)
gc = gcd(ans1, lcm)
if gc != 1:
    ans1 = ans1 // gc
    lcm = lcm // gc

print(ans1, lcm)
