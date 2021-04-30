# https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
def solution(n, t, m, timetable):
    bustime = 540
    timetable = list(map(lambda x: int(x[0]) * 60 + int(x[1]), map(lambda x: x.split(':'), timetable)))
    timetable.sort()
    idx = 0
    last = 0

    for _ in range(n):
        cnt = 0
        while cnt < m and idx + cnt < len(timetable) and timetable[idx + cnt] <= bustime:
            last = timetable[idx + cnt]
            cnt += 1

        if cnt < m:
            ans = bustime
        else:
            ans = last - 1

        idx += cnt
        bustime += t
    return '{:02d}:{:02d}'.format(ans // 60, ans % 60)


solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
solution(2, 10, 2, ["09:10", "09:09", "08:00"])
solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
