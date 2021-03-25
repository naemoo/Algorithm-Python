# https://www.acmicpc.net/problem/14391
import sys

read = sys.stdin.readline
n, m = map(int, read().strip().split())
papers = [list(map(int, read().strip())) for _ in range(n)]
ans = 0

for k in range(1 << (n * m)):
    tmp = 0
    for i in range(n):
        num = 0
        for j in range(m):
            if k & (1 << (i * m + j)) == 0:
                num = num * 10 + papers[i][j]
            else:
                tmp += num
                num = 0
        tmp += num

    for j in range(m):
        num = 0
        for i in range(n):
            if k & (1 << (i * m + j)):
                num = num * 10 + papers[i][j]
            else:
                tmp += num
                num = 0
        tmp += num
    ans = max(ans, tmp)
print(ans)
