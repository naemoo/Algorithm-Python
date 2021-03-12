# https://www.acmicpc.net/problem/1298
import sys
from collections import defaultdict

read = sys.stdin.readline
n, m = map(int, read().strip().split())
adj = defaultdict(list)

while m:
    a, b = map(int, read().strip().split())
    adj[a].append(b)
    m -= 1


def dfs(start):
    for nxt in adj[start]:
        if visit[nxt]:
            continue
        visit[nxt] = True

        if note_books[nxt] == -1 or dfs(note_books[nxt]):
            note_books[nxt] = start
            return True
    return False


ans = 0
note_books = [-1 for _ in range(n + 1)]
for person in range(1, n + 1):
    visit = [False for _ in range(n + 1)]
    if dfs(person):
        ans += 1
print(ans)