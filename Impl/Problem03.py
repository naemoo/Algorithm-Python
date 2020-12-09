#%% https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3
import re
from collections import Counter
def nGram(s):
    ngrams = []
    for i in range(0,len(s) - 1):
        ngrams.append(s[i:i+2].lower())
    ngrams = filter(lambda x : re.search('[^a-z]',x) == None, ngrams)
    return list(ngrams)
def J(A,B):
    A,B = Counter(A),Counter(B)
    inNum, unNum = sum((A&B).values()), sum((A|B).values())
    return 1 if len(A) == len(B) == 0 else inNum / unNum

def solution(str1, str2):
    A,B = nGram(str1), nGram(str2)
    return int(J(A,B) * 65536)

#%%
solution("FRANCE","french")