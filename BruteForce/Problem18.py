# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import Counter
from itertools import combinations


def solution(orders, course):
    ans = []
    for num in course:
        menu = []
        for order in orders:
            menu += combinations(sorted(order),num)
        tmp = Counter(menu).most_common()
        c = tmp[0][1] if tmp and tmp[0][1] >= 2 else -1
        for e, cnt in tmp:
            if cnt != c:
                break
            ans.append("".join(list(e)))
    ans.sort()
    return ans


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
