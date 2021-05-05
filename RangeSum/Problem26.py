# https://programmers.co.kr/learn/courses/30/lessons/67258
from collections import Counter


def solution(gems):
    end = 0
    gem_kind = len(set(gems))
    gem_cnt = Counter()
    ans = [0, float('inf')]
    for start in range(len(gems)):
        while end < len(gems) and len(gem_cnt) < gem_kind:
            gem_cnt[gems[end]] += 1
            end += 1

        if len(gem_cnt) == gem_kind and ans[1] - ans[0] > end - start - 1:
            ans[0], ans[1] = start + 1, end
        gem_cnt[gems[start]] -= 1

        if gem_cnt[gems[start]] == 0:
            del gem_cnt[gems[start]]
    return ans
