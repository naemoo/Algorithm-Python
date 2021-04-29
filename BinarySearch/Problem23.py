# https://www.acmicpc.net/problem/2539
import sys

read = sys.stdin.readline
r, c = map(int, read().strip().split())
n = int(read().strip())
wn = int(read().strip())
sites = [tuple(map(int, read().strip().split())) for _ in range(wn)]
sites.sort(key=lambda x: x[1])
sites_x = list(map(lambda x: x[1], sites))
sites_y = list(map(lambda x: x[0], sites))

l, r = 0, max(r, c)
ans = float('inf')


def canFill(size):
    start = sites_x[0]
    idx = 0
    cnt = 0
    while idx < wn:
        cnt += 1
        while idx < wn and start + size > sites_x[idx]:
            if sites_y[idx] > size:
                return False
            idx += 1
        if idx == wn:
            break
        start = sites_x[idx]
    return True if cnt <= n else False


while l <= r:
    mid = (l + r) // 2
    if canFill(mid):
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1
print(ans)
