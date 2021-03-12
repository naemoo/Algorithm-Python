# https://www.acmicpc.net/problem/16288
import sys

read = sys.stdin.readline
n, k = map(int, read().strip().split())
exits = list(map(int, read().strip().split()))
lis = [[]]
for e in exits:
    for i in range(len(lis)):
        if lis[i] and lis[i][-1] < e:
            lis[i].append(e)
            break
        elif not lis[i]:
            lis[i].append(e)
            break
        elif i == len(lis) - 1:
            lis.append([])
            lis[-1].append(e)
            break
print('YES' if len(lis) <= k else 'NO')