# https://www.acmicpc.net/problem/1167
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
v = int(read().strip())
graph = defaultdict(list)

for _ in range(v):
    infos = list(map(int, read().strip().split()))
    st = infos[0]
    idx = 1
    while infos[idx] != -1:
        graph[st].append((infos[idx], infos[idx + 1]))
        idx += 2


def getLongestVertex(start):
    q = deque()
    q.append((start, 0))
    visit = [True] * (v + 1)
    visit[start] = False
    ret = (0,0)

    while q:
        cur, w = q.popleft()

        for nxt,nw in graph[cur]:
            if visit[nxt]:
                q.append((nxt, w + nw))
                visit[nxt] = False
                if w + nw > ret[0]:
                    ret = nw + w,nxt

    return ret

w,x = getLongestVertex(1)
w,y = getLongestVertex(x)
print(w)
