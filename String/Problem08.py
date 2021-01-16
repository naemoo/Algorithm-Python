# https://www.acmicpc.net/problem/4358
import sys
from collections import defaultdict

read = sys.stdin.readline
trees = defaultdict(int)
tree = read().strip()
total = 0

while tree:
    tree.upper()
    trees[tree] += 1
    total += 1
    tree = read().strip()

for k, v in sorted(trees.items()):
    print(k, round(v * 100 / total, 4))
