# https://www.acmicpc.net/problem/1339
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
arr = [read().strip() for _ in range(n)]
score = defaultdict(int)

for e in arr:
    for i in range(len(e)):
        score[e[i]] += 10 ** (len(e) - i - 1)

num = 9
ret = 0
for k,v in sorted(score.items(), key=lambda x: -x[1]):
    ret += num * v
    num -= 1

print(ret)