# https://www.acmicpc.net/problem/5549
import sys

read = sys.stdin.readline
m, n = map(int, read().strip().split())
k = int(read().strip())
planets = [read().strip() for _ in range(m)]
j_maps = list(map(lambda x: list(map(lambda e: 1 if e == 'J' else 0, x)), planets))
i_maps = list(map(lambda x: list(map(lambda e: 1 if e == 'I' else 0, x)), planets))
o_maps = list(map(lambda x: list(map(lambda e: 1 if e == 'O' else 0, x)), planets))
j_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
i_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
o_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        j_sum[i][j] = j_sum[i - 1][j] + j_sum[i][j - 1] - j_sum[i - 1][j - 1] + j_maps[i - 1][j - 1]
        i_sum[i][j] = i_sum[i - 1][j] + i_sum[i][j - 1] - i_sum[i - 1][j - 1] + i_maps[i - 1][j - 1]
        o_sum[i][j] = o_sum[i - 1][j] + o_sum[i][j - 1] - o_sum[i - 1][j - 1] + o_maps[i - 1][j - 1]


def getSum(arr):
    global a, b, c, d
    return arr[c][d] - arr[c][b - 1] - arr[a - 1][d] + arr[a - 1][b - 1]


while k:
    a, b, c, d = map(int, read().strip().split())
    j, o, i = getSum(j_sum), getSum(o_sum), getSum(i_sum)
    print(j, o, i)
    k -= 1
