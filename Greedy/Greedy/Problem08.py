# https://www.acmicpc.net/problem/1826
import heapq
import sys

read = sys.stdin.readline
n = int(read().strip())
stations = [tuple(map(int, read().strip().split())) for _ in range(n)]
l, gas = map(int, read().strip().split())

cur, idx = 0, 0
nxtIdx = 0
cnt = 0
q = []
stations.sort()
stations.insert(0, (0, 0))
stations.append((l, 0))


def lower(arr, target):
    l, r = 0, len(arr),

    while l < r:
        mid = (l + r) // 2
        if arr[mid][0] < target:
            l = mid + 1
        else:
            r = mid
    return r


while cur < l:
    nxtIdx = lower(stations, cur + gas)

    if nxtIdx >= len(stations):
        break

    if stations[nxtIdx][0] > cur + gas:
        nxtIdx -= 1

    if nxtIdx == idx:
        if q:
            gas += -heapq.heappop(q)
            cnt += 1
        else:
            cnt = -1
            break
    else:
        for i in range(idx + 1, nxtIdx + 1):
            heapq.heappush(q, -stations[i][1])
        idx = nxtIdx
        gas -= (stations[nxtIdx][0] - cur)
        cur = stations[nxtIdx][0]

print(cnt)
