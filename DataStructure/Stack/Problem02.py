# https://www.acmicpc.net/problem/3425
import sys

read = sys.stdin.readline
cmd = read().strip()

while cmd != 'QUIT':
    logs = []
    while cmd != 'END':
        logs.append(cmd)
        cmd = read().strip()
    n = int(read().strip())
    for _ in range(n):
        isError = False
        s = []
        s.append(int(read().strip()))

        try:
            for log in logs:
                if log[:3] == 'NUM':
                    x = int(log.split()[1])
                    s.append(x)
                elif log[:3] == 'POP':
                    s.pop()
                elif log[:3] == 'INV':
                    s[-1] = -s[-1]
                elif log[:3] == 'DUP':
                    s.append(s[-1])
                elif log[:3] == 'SWP':
                    s[-1], s[-2] = s[-2], s[-1]
                elif log[:3] == 'ADD':
                    a, b = s.pop(), s.pop()
                    if abs(b + a) > 10 ** 9:
                        isError = True
                        break
                    s.append(a + b)
                elif log[:3] == 'SUB':
                    a, b = s.pop(), s.pop()
                    if abs(b - a) > 10 ** 9:
                        isError = True
                        break
                    s.append(b - a)
                elif log[:3] == 'MUL':
                    a, b = s.pop(), s.pop()
                    if abs(a * b) > 10 ** 9:
                        isError = True
                        break
                    s.append(a * b)
                elif log[:3] == 'DIV':
                    a, b = s.pop(), s.pop()
                    if a == 0:
                        isError = True
                        break
                    tmp = abs(b) // abs(a)
                    tmp = tmp * -1 if a * b < 0 else tmp
                    s.append(tmp)
                elif log[:3] == 'MOD':
                    a, b = s.pop(), s.pop()
                    if a == 0:
                        isError = True
                        break
                    tmp = abs(b) % abs(a)
                    tmp = tmp * -1 if b < 0 else tmp
                    s.append(tmp)
        except:
            isError = True
        if len(s) != 1 or isError:
            print('ERROR')
        else:
            print(s.pop())
    read().strip()
    print()
    cmd = read().strip()
