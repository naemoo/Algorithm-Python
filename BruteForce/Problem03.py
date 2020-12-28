# https://www.acmicpc.net/problem/1940
import sys
inp = sys.stdin.readline
n = int(inp().strip())
m = int(inp().strip())
materials = [int(e) for e in inp().strip().split()]

left, right = 0, len(materials) - 1
materials.sort()
ans = 0
while left < right:
    armor = materials[left] + materials[right]
    if armor < m:
        left += 1
    elif armor > m:
        right -= 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)

