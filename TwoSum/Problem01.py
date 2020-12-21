# https://www.acmicpc.net/problem/2467
import sys

inp = sys.stdin.readline
n = int(inp())
solution = [e for e in map(int, inp().strip().split())]
l, r = 0, len(solution) - 1
ans = (float('inf'), 0, 0)

while l < r:
    combinations = abs(solution[l] + solution[r])
    if combinations < ans[0]:
        ans = combinations, solution[l], solution[r]
    if abs(solution[l]) < abs(solution[r]):
        r -= 1
    else:
        l += 1
print(ans[1],ans[2])
