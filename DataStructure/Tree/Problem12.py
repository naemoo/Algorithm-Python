# https://programmers.co.kr/learn/courses/30/lessons/72416
from collections import defaultdict
import sys

max_num = 300006
sys.setrecursionlimit(max_num)


def go(cur, adj, dp, sales):
    ret = [None, sales[cur]]
    tmp = 0
    if cur in adj.keys():
        for nxt in adj[cur]:
            t = go(nxt, adj, dp, sales)
            tmp += min(t)
    for nxt in adj[cur]:
        ret[1] += min(dp[nxt])
        if ret[0] != None:
            ret[0] = min(tmp - min(dp[nxt]) + dp[nxt][1], ret[0])
        else:
            ret[0] = tmp - min(dp[nxt]) + dp[nxt][1]
    ret[0] = 0 if ret[0] == None else ret[0]
    dp[cur] = ret
    return ret


def solution(sales, links):
    sales.insert(0, 0)
    adj = defaultdict(list)
    dp = [[-1 for _ in range(2)] for _ in range(max_num)]
    for a, b in links:
        adj[a].append(b)
    return min(go(1, adj, dp, sales))


ans = solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])
# ans = solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]])
print(ans)
