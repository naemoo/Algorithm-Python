# https://www.acmicpc.net/problem/5568
import sys
from itertools import permutations

read = sys.stdin.readline
n = int(read().strip())
k = int(read().strip())

cards = [read().strip() for _ in range(n)]
ret = set()
for e in permutations(cards, k):
    ret.add("".join(e))
print(len(ret))
