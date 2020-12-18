#%% https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
import re
def splitString(s):
    cnt = [0,0]
    for i in range(len(s)):
        if s[i] == '(':
            cnt[0] += 1
        else:
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            return s[0:i+1],s[i+1:]
def isRightBalance(s):
    while '()' in s:
        s = re.sub('\(\)',"",s)
    return True if len(s) == 0 else False

def transBalance(p):
    if len(p) == 0:
        return ""
    elif isRightBalance(p):
        return p
    u,v = splitString(p)
    if isRightBalance(u):
        return u + transBalance(v)
    else:
        return '(' + "".join(map(lambda x : ')' if x == '(' else '(',u[1:-1])) + ')' + transBalance(v)

def solution(p):
    print(transBalance(p))
#%%
solution("(()())()")
