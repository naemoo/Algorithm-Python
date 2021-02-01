# https://www.acmicpc.net/problem/3649
import sys

read = sys.stdin.readline
while True:
    try:
        width = int(read().strip()) * 10000000
        n = int(read().strip())
        blocks = [int(read().strip()) for _ in range(n)]
        blocks.sort()
        isAns = False

        l, r = 0, n - 1
        while l < r:
            tmp = blocks[l] + blocks[r]
            if tmp == width:
                isAns = True
                break
            elif tmp > width:
                r -= 1
            else:
                l += 1

        if isAns:
            print('yes %d %d' % (blocks[l], blocks[r]))
        else:
            print('danger')
    except:
        break