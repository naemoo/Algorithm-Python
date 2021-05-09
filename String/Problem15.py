# https://www.acmicpc.net/problem/8913
import re

def solve(s):
    group = [(m.start(0), m.end(0)) for m in re.finditer('aa+|bb+', s)]
    if len(group) == 0: return 0
    if len(set(s)) == 1: return 1
    for g in group:
        if solve(s[0:g[0]] + s[g[1]:]) == 1: return 1
    return 0

strings = [input() for _ in range(int(input()))]
for string in strings:
    print(solve(string))
