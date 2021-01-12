# %% https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3
def jump(target, rocks, n):
    idx = 0
    j = 1
    cnt = 0
    while idx + j < len(rocks):
        while idx + j < len(rocks) and rocks[idx + j] - rocks[idx] < target:
            j += 1
            cnt += 1
        idx += j
        j = 1
    return True if cnt <= n else False


# %%
def lower(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


def jump(target, rocks, n):
    cnt = 0
    i = 0
    while i < len(rocks):
        idx = lower(rocks, rocks[i] + target)
        cnt += idx - i - 1
        i = idx

    return True if cnt <= n else False


def solution(distance, rocks, n):
    l, r = 1, distance
    rocks.insert(0, 0)
    rocks.append(distance)
    rocks.sort()
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if jump(mid, rocks, n):
            ans = max(ans, mid)
            l = mid + 1
        else:
            r = mid - 1
    return ans


a = solution(25, [24], 2)
print(a)
