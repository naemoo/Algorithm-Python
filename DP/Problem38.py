# https://www.acmicpc.net/problem/2749
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = [[1, 1], [1, 0]]


def mul(arr1, arr2):
    ret = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for k in range(2):
            for j in range(2):
                ret[i][j] = (ret[i][j] + arr1[i][k] * arr2[k][j]) % 1000000
    return ret


def mul_n(arr1, k):
    if k == 2:
        return mul(arr, arr)
    elif k == 1:
        return arr

    half_arr = mul_n(arr1, k // 2)
    if k % 2:
        ret = mul(mul(half_arr, half_arr), arr)
    else:
        ret = mul(half_arr, half_arr)
    return ret


if n >= 2:
    print(mul_n(arr, n - 1)[0][0])
else:
    print(n)
