# https://www.acmicpc.net/problem/16562
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 1)
read = sys.stdin.readline
n, m, k = map(int, read().strip().split())
costs = list(map(int, read().strip().split()))

friends = [[i, 0] for i in range(n)]


def find(idx):
    if friends[idx][0] == idx:
        return idx
    friends[idx][0] = find(friends[idx][0])
    return friends[idx][0]


def merge(a, b):
    a, b = find(a), find(b)
    if friends[a][1] < friends[b][1]:
        friends[a][0] = b
    elif friends[a][1] > friends[b][1]:
        friends[b][0] = a
    else:
        friends[a][0] = b
        friends[b][1] += 1


for _ in range(m):
    a, b = map(int, read().strip().split())
    merge(a - 1, b - 1)

friend_cost = defaultdict(lambda: float('inf'))
for i in range(n):
    root = find(i)
    friend_cost[root] = min(friend_cost[root], costs[i])
ans = sum(friend_cost.values())
print(ans if ans <= k else 'Oh no')
