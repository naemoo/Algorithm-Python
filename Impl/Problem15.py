# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

read = sys.stdin.readline
test = int(read().strip())
while test:
    commands = read().strip()
    isReverse = False
    flag = True
    n = int(read().strip())
    arr = deque(read().strip().strip('[]').split(','))
    if len(arr) == 1 and not arr[-1].isdigit():
        arr.pop()

    for command in commands:
        if command == 'R':
            isReverse = isReverse ^ (not isReverse)
        else:
            try:
                if isReverse:
                    arr.pop()
                else:
                    arr.popleft()
            except:
                flag = False
    if isReverse:
        arr.reverse()
    print('[' + (','.join(arr)) + ']' if flag else 'error')
    test -= 1


