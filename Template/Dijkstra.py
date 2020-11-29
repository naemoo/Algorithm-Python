import heapq
paths = {{}}
INF = float('inf')
v = 4;

def dijkstra(start):
    length = [INF] * (v+1)
    length[start] = 0
    q = []
    q.put((0,start))

    while q:
        w,cur = heapq.heappush(q,(0,start))
        if length[cur] < w:
            continue

        for nxt,nw in paths[cur].items():
            nextDistance = nw + w
            if nextDistance < length[nxt]:
                length[nxt] = nextDistance
                heapq.heappush(q,(nextDistance,nxt))
    return length