# https://programmers.co.kr/learn/courses/30/lessons/72412
import re
from bisect import bisect_left
from collections import defaultdict
from itertools import product
d = (('java', 'python', 'cpp'), ('backend', 'frontend'), ('junior', 'senior'), ('pizza', 'chicken'))


def solution(info, query):
    volunteer = defaultdict(list)
    ret = []
    for e in info:
        e = e.split()
        score = int(e[-1])
        del e[-1]
        volunteer[tuple(e)].append(score)
    for v, k in volunteer.items():
        k.sort()
    for q in query:
        q = re.split('\sand\s|\s', q)
        score = int(q[-1])
        del q[-1]
        search = []
        for i, case in enumerate(q):
            if case == '-':
                search.append(d[i])
            else:
                search.append([case])
        cnt = 0
        for e in product(*search):
            arr = volunteer[e]
            cnt += (len(arr) - bisect_left(arr, score))
        ret.append(cnt)
    return ret

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
