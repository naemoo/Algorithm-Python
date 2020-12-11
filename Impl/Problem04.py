# %% https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
import re
os = 999

def getMillSec(time):
    t, m, sec, msec = map(int, re.split('[:.]', time))
    msec += (sec * 1000 + m * 60 * 1000 + t * 60 * 60 * 1000)
    return msec

def solution(lines):
    logs = []
    for line in lines:
        dateInfo = line.split()
        end = getMillSec(dateInfo[1])
        doTime = int(float(dateInfo[2][:-1]) * 1000)
        start = end - doTime + 1
        logs.append((start, end))
    ans = 0
    for ps, pe in logs:
        cnt1, cnt2 = 0, 0
        for cs, ce in logs:
            s, e = ps-os, pe+os
            if not (ce < s or ps < cs):
                cnt1 += 1
            if not(ce < pe or e < cs):
                cnt2 += 1
        ans = max(ans, max(cnt1, cnt2))
    return ans


solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
          "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
