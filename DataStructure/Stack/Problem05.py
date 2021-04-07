# https://www.acmicpc.net/problem/2504
import sys

read = sys.stdin.readline
cmd = read().strip()
s = []
score = 0

for e in cmd:
    if e == ')':
        tmp = 0
        while s and s[-1] != '(':
            e = s.pop()

            if len(s) == 0 or e == ')' or e == '[':
                print(0)
                sys.exit()
            if type(e) == int:
                tmp += e
        if tmp == 0:
            tmp = 1

        if len(s) == 0:
            print(0)
            sys.exit()

        s.pop()
        s.append(tmp * 2)

    elif e == ']':
        tmp = 0
        while s and s[-1] != '[':
            e = s.pop()
            if len(s) == 0 or e == ']' or e == '(':
                print(0)
                sys.exit()
            if type(e) == int:
                tmp += e

        if tmp == 0:
            tmp = 1

        if len(s) == 0:
            print(0)
            sys.exit()

        s.pop()
        s.append(tmp * 3)
    else:
        s.append(e)

while s:
    if type(s[-1]) != int:
        print(0)
        sys.exit()
    score += s.pop()
print(score)
