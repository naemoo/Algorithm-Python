# https://www.acmicpc.net/problem/2116
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10005)
n = int(read().strip())
dices = []
across = {0: 5, 1: 3, 2: 4, 4: 2, 3: 1, 5: 0}

for _ in range(n):
    dices.append(list(map(int, read().strip().split())))

ans = 0


def go(d, bottom, score):
    global ans
    if d == n:
        ans = max(ans, score)
        return

    b_idx = dices[d].index(bottom)
    u_idx = across[b_idx]
    tmp = max(map(lambda x: x[1], filter(lambda x: not x[0] in (b_idx, u_idx), enumerate(dices[d]))))
    go(d + 1, dices[d][u_idx], score + tmp)


for bottom in range(6):
    score = max(map(lambda x: x[1], filter(lambda x: not x[0] in (bottom, across[bottom]), enumerate(dices[0]))))
    go(1, dices[0][bottom], score)

print(ans)
