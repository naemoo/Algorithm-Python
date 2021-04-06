# https://www.acmicpc.net/problem/17609
import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 5)
n = int(read().strip())
words = [read().strip() for _ in range(n)]


def isPalindrome(start, end, cnt=0):
    if start >= end:
        return True
    ret = False
    if word[start] == word[end]:
        ret = isPalindrome(start + 1, end - 1, cnt)
    elif cnt == 0:
        ret = isPalindrome(start + 1, end, 1) | isPalindrome(start, end - 1, 1)

    return ret


for word in words:
    l, r = 0, len(word) - 1
    flag = False
    while l < r:
        if word[l] != word[r]:
            flag = True
            break
        l += 1
        r -= 1
    if flag:
        print(1 if isPalindrome(l, r) else 2)
    else:
        print(0)
