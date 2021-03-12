# https://www.acmicpc.net/problem/10828
import sys

read = sys.stdin.readline
n = int(read().strip())
s = []

for _ in range(n):
    cmd = read().strip()
    if cmd[:4] == "push":
        num = int(cmd.split()[1])
        s.append(num)
    elif cmd == "pop":
        print(-1 if len(s) == 0 else s.pop())
    elif cmd == "size":
        print(len(s))
    elif cmd == "empty":
        print(1 if len(s) == 0 else 0)
    elif cmd == "top":
        print(-1 if len(s) == 0 else s[-1])
