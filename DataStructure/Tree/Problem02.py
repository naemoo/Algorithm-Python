# https://programmers.co.kr/learn/courses/30/lessons/68937
from collections import defaultdict, deque


def getShortest(start, tree, n):
    q = deque()
    q.append((0, start))
    visit = [True] * (n + 1)
    visit[start] = False
    m, cnt, idx = -1, 0, start

    while q:
        w, cur = q.popleft()
        if m < w:
            m, cnt, idx = w, 1, cur
        elif m == w:
            cnt += 1

        for nxt in tree[cur]:
            if visit[nxt]:
                q.append((w + 1, nxt))
                visit[nxt] = False
    return idx, cnt, m


def solution(n, edges):
    tree = defaultdict(list)
    for st, to in edges:
        tree[st].append(to)
        tree[to].append(st)

    x, cnt, m = getShortest(1, tree, n)
    y, cnt, m = getShortest(x, tree, n)
    ans = cnt
    z, cnt, m = getShortest(y, tree, n)
    ans = max(ans, cnt)
    return m if cnt > 1 else m - 1


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
