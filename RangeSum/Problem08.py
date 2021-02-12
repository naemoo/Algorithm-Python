# https://www.acmicpc.net/problem/2632
import sys
from bisect import bisect_left, bisect_right

read = sys.stdin.readline
order = int(read().strip())
n, m = map(int, read().strip().split())
a_foods = [int(read().strip()) for _ in range(n)]
b_foods = [int(read().strip()) for _ in range(m)]
a_sum = [0 for _ in range(n + 1)]
b_sum = [0 for _ in range(m + 1)]
for i in range(1, n + 1):
    a_sum[i] = a_sum[i - 1] + a_foods[i - 1]

for i in range(1, m + 1):
    b_sum[i] = b_sum[i - 1] + b_foods[i - 1]

def getCombinations(isA, n):
    ret = [0]
    arr = a_sum if isA else b_sum
    for num in range(1, n + 1):
        if num == n:
            ret.append(arr[n])
            break

        for i in range(n):
            tmp = 0
            if i + num > n:
                tmp = arr[n] - arr[i] + arr[(i + num) % n]
            else:
                tmp = arr[i + num] - arr[i]
            ret.append(tmp)
    return ret


a_combinations = getCombinations(True, n)
b_combinations = getCombinations(False, m)
b_combinations.sort()
ans = 0
for a_combination in a_combinations:
    tmp = order - a_combination
    ans += bisect_right(b_combinations, tmp) - bisect_left(b_combinations, tmp)

print(ans)
