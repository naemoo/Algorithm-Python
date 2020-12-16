# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3
import re
def solution(files):
    answer = []
    for file in files:
        m = re.search('\d+',file)
        f = (file[:m.start()].lower(), int(m.group()),file[m.end():],file)
        answer.append(f)
    return list(map(lambda x : x[3],sorted(answer, key = lambda x : (x[0],x[1]))))
        
        
                
