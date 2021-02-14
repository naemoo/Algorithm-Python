# https://www.acmicpc.net/problem/10830
import sys

read = sys.stdin.readline
n, b = map(int, read().strip().split())
arr = [list(map(int, read().strip().split())) for _ in range(n)]


def mul(arr1, arr2):
    ret = [([0] * n) for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                ret[i][j] += arr1[i][k] * arr2[k][j]
                ret[i][j] %= 1000
    return ret


def mulArr(arr, b):
    if b == 2:
        return mul(arr, arr)
    elif b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    half_arr = mulArr(arr, b // 2)
    if b % 2:
        ret = mul(mul(half_arr, half_arr), arr)
    else:
        ret = mul(half_arr, half_arr)
    return ret


for es in mulArr(arr, b):
    for e in es:
        print(e, end=' ')
    print()
