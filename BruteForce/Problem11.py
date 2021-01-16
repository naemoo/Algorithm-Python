# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations

read = sys.stdin.readline
l, c = map(int, read().strip().split())
arr = [e for e in read().strip().split()]
collections = {'a', 'e', 'i', 'o', 'u'}
arr.sort()

for e in combinations(arr, l):
    s1 = set(e)
    tmp = s1 & collections # 모음
    if len(tmp) >= 1 and l - len(tmp) >=2:
        print("".join(e))
