# https://programmers.co.kr/learn/courses/30/lessons/64064
import re
from itertools import permutations
def solution(user_id, banned_id):
    for i in range(len(banned_id)):
        banned_id[i] = re.sub('\*','.',banned_id[i])
    users = permutations(user_id,len(banned_id))
    answer = set()
    for user in users:
        cnt = 0
        for i in range(len(user)):
            if re.fullmatch(banned_id[i],user[i]) != None:
                cnt+=1
        if cnt == len(banned_id):
            answer.add(tuple(sorted(user)))
    print(answer)
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])