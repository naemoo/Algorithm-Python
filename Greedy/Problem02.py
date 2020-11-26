from queue import PriorityQueue
from collections import defaultdict
import sys
INF = float('inf')
v,n = map(int, sys.stdin.readline().strip().split())
paths = defaultdict(defaultdict)

for _ in range(n):
    start,end,w = map(int, sys.stdin.readline().strip().split())
    paths[start][end] = w
    paths[end][start] = w

a,b = map(int, sys.stdin.readline().strip().split())

def dijkstra(start):
    length = [INF] * (v+1)
    length[start] = 0
    q = PriorityQueue()
    q.put((0,start))

    while not q.empty():
        w,cur = q.get()
        if length[cur] < w:
            continue

        for nxt,nw in paths[cur].items():
            nextDistance = nw + w
            if nextDistance < length[nxt]:
                length[nxt] = nextDistance
                q.put((nextDistance,nxt))
    return length

d0 = dijkstra(1)
d1 = dijkstra(a)
d2 = dijkstra(b)

path1 = d0[a] + d1[b] + d2[v]
path2 = d0[b] + d2[a] + d1[v]

answer = min(path1,path2)

print(answer if answer != INF else -1)