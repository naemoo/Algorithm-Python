# https://programmers.co.kr/learn/courses/30/lessons/12979
import math


def solution(n, stations, w):
    ans = math.ceil((stations[0] - w - 1) / (2 * w + 1))
    end = (n - (stations[-1] + w))
    if end > 0:
        ans += math.ceil(end / (2 * w + 1))

    for i in range(len(stations) - 1):
        e = stations[i + 1] - stations[i] - 2 * w - 1
        if e > 0:
            ans += math.ceil(end / (w + 2))
    print(ans)
    return ans


solution(16, [9], 2)
