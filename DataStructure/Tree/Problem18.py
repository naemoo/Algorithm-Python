# https://programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    adj = dict(zip(enroll, referral))
    profits = defaultdict(int)

    def getProfit(sell, money):
        cur = sell
        while cur != '-':
            parent_money = money // 10
            profits[cur] += money - parent_money
            money = parent_money
            cur = adj[cur]

    for sell, money in zip(seller, amount):
        getProfit(sell, money * 100)

    return list(map(lambda x: profits[x], enroll))


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
