# https://programmers.co.kr/learn/courses/30/lessons/67257
from copy import deepcopy
from itertools import permutations
import re


def solution(expression):
    ans = 0
    cp_nums = list(map(int, re.split('[*+-]', expression)))
    cp_ops = re.findall('[-*+]', expression)
    for ops in permutations(set(cp_ops), len(set(cp_ops))):
        opr = deepcopy(cp_ops)
        nums = deepcopy(cp_nums)
        for e in ops:
            while e in opr:
                i = opr.index(e)
                opr.pop(i)
                if e == '*':
                    tmp = nums.pop(i) * nums.pop(i)
                elif e == '+':
                    tmp = nums.pop(i) + nums.pop(i)
                elif e == '-':
                    tmp = nums.pop(i) - nums.pop(i)
                nums.insert(i, tmp)
        ans = max(abs(nums[0]), ans)
    return ans


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
