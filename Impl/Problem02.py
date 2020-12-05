# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
from collections import Counter
def solution(N, stages):
    cnt = Counter(stages)
    failure = [[0, i] for i in range(1, N+1)]
    for st, cn in cnt.items():
        for i in range(1, st+1):
            if i <= N:
                failure[i-1][0] += cn

    for i in range(1, N+1):
        if i in cnt.keys():
            failure[i-1][0] = cnt[i] / failure[i-1][0]
        else:
            failure[i-1][0] = 0
    return list(map(lambda x: x[1], sorted(failure, key=lambda x: (-x[0], x[1]))))

# %%
solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4,	[4, 4, 4, 4, 4])
