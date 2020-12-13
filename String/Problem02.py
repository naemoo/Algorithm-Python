#https://programmers.co.kr/learn/courses/30/lessons/64065
import re
from collections import Counter 
def solution(s):
    c = Counter(re.findall('\d+',s))
    return [int(k) for k,v in sorted(c.items(),key = lambda x : x[1],reverse = True)]