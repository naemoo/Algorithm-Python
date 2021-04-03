# https://www.acmicpc.net/problem/14505
import sys

read = sys.stdin.readline
word = read().strip()
n = len(word)
dp = [[-1 for _ in range(n)] for _ in range(n)]


def get_palindrome(start, end):
    if start >= end:
        return 1 if start == end else 0
    if dp[start][end] != -1:
        return dp[start][end]

    ret = 0
    if word[start] == word[end]:
        ret = get_palindrome(start + 1, end) + get_palindrome(start, end - 1) + 1
    else:
        ret = get_palindrome(start + 1, end) + get_palindrome(start, end - 1) - get_palindrome(start + 1, end - 1)
    dp[start][end] = ret
    return ret


print(get_palindrome(0, n - 1))
