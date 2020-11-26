# https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq
from collections import defaultdict
def solution(N, road, K):
    roads = defaultdict(lambda : defaultdict(lambda : float('inf')))

    for start,end,weight in road:
        prev = min(roads[start][end],weight)
        roads[start][end] = min(prev,weight)
        roads[end][start] = min(prev,weight)

    length = [float('inf')] * (N+1)
    length[1]  = 0 
    q = []
    heapq.heappush(q,(0,1))

    while q:
        w,cur = heapq.heappop(q)
        if length[cur] < w:
            continue

        length[cur] = w

        for nextC, nW in roads[cur].items():
            nextWeight = nW + w
            if length[nextC] > nextWeight:
                heapq.heappush(q,(nextWeight,nextC))

    answer = 0
    for k in length:
        answer += 1 if k <= K else 0

    return answer
# %%
solution(5,[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],3)
