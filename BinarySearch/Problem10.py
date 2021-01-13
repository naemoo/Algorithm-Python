# https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3
def canGo(arr, target, k):
    cur = -1
    nxt = 1
    while cur < len(arr):
        while cur + nxt < len(arr) and arr[cur + nxt] < target:
            nxt += 1

        if nxt > k:
            return False
        cur += nxt
        nxt = 1
    return True


def solution(stones, k):
    l, r = min(stones), max(stones)

    ret = 0
    while l < r:
        mid = (l + r) // 2

        if canGo(stones, mid, k):
            ret = max(ret, mid)
            l = mid + 1
        else:
            r = mid - 1
    return l


a = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print(ret)
