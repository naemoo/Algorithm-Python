# https://programmers.co.kr/learn/courses/30/lessons/72414

def timeToSec(play_time):
    h, m, s = map(int, play_time.split(":"))
    return h * 60 * 60 + m * 60 + s


def secToTime(sec):
    h = sec // (60 * 60)
    sec = sec % (60 * 60)
    m = sec // 60
    s = sec % 60
    return "%02d:%02d:%02d" % (h, m, s)


def solution(play_time, adv_time, logs):
    play_sec = timeToSec(play_time)
    adv_sec = timeToSec(adv_time)
    t = [0 for _ in range(play_sec + 1)]
    s = [0 for _ in range(play_sec + 2)]
    ss = [0 for _ in range(play_sec + 2)]

    for log in logs:
        st, end = map(timeToSec, log.split("-"))
        t[st] += 1
        t[end] -= 1

    for i in range(1, play_sec + 2):
        s[i] = s[i - 1] + t[i - 1]

    for i in range(1, play_sec + 2):
        ss[i] = ss[i - 1] + s[i]

    tmp = 0
    ret = 0
    for i in range(play_sec - adv_sec + 1):
        if ss[i + adv_sec] - ss[i] > tmp:
            ret = i
            tmp = ss[i + adv_sec] - ss[i]
    print(secToTime(ret))


# solution("02:03:55", "00:14:15",
#          ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
# solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
