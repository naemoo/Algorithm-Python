# https://www.acmicpc.net/problem/2467
import sys

inp = sys.stdin.readline
n = int(inp())
solution = [e for e in map(int, inp().strip().split())]
ans = (float('inf'), 0, 0)

for i in range(len(solution)):
    l, r = i + 1, len(solution) - 1
    while l <= r:
        mid = (l + r) // 2
        if abs(solution[i] + solution[mid]) < ans[0]:
            ans = abs(solution[i] + solution[mid]), solution[i], solution[mid]

        if solution[i] + solution[mid] < 0:
            l = mid + 1
        else:
            r = mid - 1
print(ans[1], ans[2])
