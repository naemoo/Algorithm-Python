# https://www.acmicpc.net/problem/10653
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
check_points = [list(map(int, read().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(k + 1)] for _ in range(n)]


def getDistance(start, end):
    start, end = map(lambda x: check_points[x], (start, end))
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def go(d, skip):
    if d == n - 1:
        return 0
    if dp[d][skip] != -1:
        return dp[d][skip]

    ret = float('inf')
    for i in range(k - skip + 1):
        if d + 1 + i < n:
            ret = min(ret, go(d + 1 + i, skip + i) + getDistance(d, d + 1 + i))
    dp[d][skip] = ret
    return ret


print(go(0, 0))

# directions = []
# for i in range(1, k + 1):
#     directions.append((0 + i, i - 1))
# q = [(0, 0, 0)]
# visit = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
# visit[0][0] = 0
#
# while q:
#     cost, cur, skip = heappop(q)
#
#     if visit[cur][skip] < cost:
#         continue
#
#     for step, sk in directions:
#         nxt = cur + step
#         nxt_skip = skip + sk
#
#         if nxt >= n or nxt_skip > k:
#             continue
#         nxt_cost = getDistance(cur, nxt) + cost
#         if nxt_cost < visit[nxt][nxt_skip]:
#             heappush(q, (nxt_cost, nxt, nxt_skip))
#             visit[nxt][nxt_skip] = nxt_cost
# print(min(visit[n - 1]))
