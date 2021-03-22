# https://www.acmicpc.net/problem/10942
import sys

read = sys.stdin.readline
n = int(read().strip())
arr = list(map(int, read().strip().split()))
m = int(read().strip())
dp = [[None for _ in range(n)] for _ in range(n)]


def isPalindrome(start, end):
    if start >= end:
        return True

    if dp[start][end] != None:
        return dp[start][end]

    if arr[start] == arr[end]:
        ret = isPalindrome(start + 1, end - 1)
    else:
        ret = False
    dp[start][end] = ret
    return ret


while m:
    a, b = map(int, read().strip().split())
    ans = 1 if isPalindrome(a - 1, b - 1) else 0
    print(ans)
    m -= 1
