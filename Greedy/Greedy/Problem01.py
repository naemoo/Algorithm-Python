# https://www.acmicpc.net/problem/1931
import sys

inp = sys.stdin.readline
n = int(inp())
meetRooms = []
for _ in range(n):
    st,to = map(int,inp().strip().split())
    meetRooms.append((st,to))

cur,ans = 0,0
meetRooms = sorted(meetRooms, key = lambda x : (x[1],x[0]))
for ms,me in meetRooms:
    if cur <= ms:
        ans += 1
        cur = me
print(ans)