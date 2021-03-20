# https://www.acmicpc.net/problem/1102
import sys

read = sys.stdin.readline
n = int(read().strip())
costs = [list(map(int, read().strip().split())) for _ in range(n)]
plant = sum(list(map(lambda x: 0 if x[1] == 'N' else 1 << x[0], enumerate(list(read().strip())))))
p = int(read().strip())
dp = [-1 for _ in range(1 << n)]


def go(state):
    cnt = get_cnt(state)
    if cnt == p:
        return 0
    if dp[state] != -1:
        return dp[state]

    ret = float('inf')
    for cur in range(n):
        if state & (1 << cur):
            for nxt in range(n):
                if state & (1 << nxt):
                    continue
                ret = min(go(state | (1 << nxt)) + costs[cur][nxt], ret)
    dp[state] = ret
    return ret


def get_cnt(state):
    ret = 0
    for i in range(n):
        if state & (1 << i):
            ret += 1
    return ret


if get_cnt(plant) >= p:
    print(0)
    sys.exit()

go(plant)
print(dp[plant] if dp[plant] != float('inf') else -1)
