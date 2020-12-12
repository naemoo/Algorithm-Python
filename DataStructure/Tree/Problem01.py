# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict,deque
inp = sys.stdin.readline
n = int(inp())
tree = defaultdict(defaultdict)
for _ in range(n-1):
    st,to,w = map(int,inp().strip().split())
    tree[st][to] = w
    tree[to][st] = w

def getLongestPath(start):
    q = deque()
    q.append((0,start))
    visit = [True] * (n+1)
    visit[start] = False
    maxIdx, max = start,0

    while q:
        w, cur = q.popleft()

        if cur in tree.keys():
            for nxt,nw in tree[cur].items():
                if visit[nxt]:
                    q.append((nw+w, nxt))
                    visit[nxt] = False
                    if max < nw+w :
                        max,maxIdx = nw+w, nxt
    return maxIdx, max

x,len = getLongestPath(1)
y,len = getLongestPath(x)
print(len)