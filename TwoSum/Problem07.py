# https://www.acmicpc.net/problem/15961
import sys
from collections import Counter

read = sys.stdin.readline
n, d, k, c = map(int, read().strip().split())
sushi = [int(read().strip()) for _ in range(n)]
sushi += sushi[:k - 1]
end = 0
kinds = Counter([c])
ans = 0

for start in range(len(sushi)):

    while end < len(sushi) and end - start < k:
        kinds[sushi[end]] += 1
        end += 1

    ans = max(ans, len(kinds))

    kinds[sushi[start]] -= 1
    if kinds[sushi[start]] == 0:
        del kinds[sushi[start]]

print(ans)