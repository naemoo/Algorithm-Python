# https://www.acmicpc.net/problem/1722
import sys

read = sys.stdin.readline
n = int(read().strip())
cmd = list(map(int, read().strip().split()))
cmd[0] -= 1

fact = [-1 for _ in range(21)]
fact[0] = 1
for i in range(1, 21):
    fact[i] = fact[i - 1] * i


def go(d, ans):
    global k, arr, fact
    if d == n:
        print(" ".join(map(str, ans)))
        sys.exit()

    c = len(arr)
    cnt = fact[c - 1]
    for i in range(c):
        if k <= (i + 1) * cnt:
            ans.append(arr[i])
            arr.pop(i)
            k -= i * cnt
            go(d + 1, ans)


def binary(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r


if cmd[0]:
    # 몇 번째인지 찾기
    ret = 0
    arr = list(range(1, n + 1))
    for e in cmd[1:]:
        n -= 1
        idx = binary(arr, e)
        arr.pop(idx)
        ret += fact[n] * idx
    print(ret + 1)

else:
    # 순열 찾기
    k = cmd[1]
    arr = list(range(1, n + 1))
    go(0, [])
