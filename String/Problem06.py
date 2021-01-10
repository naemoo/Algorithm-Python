# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    userInfo = dict()
    logs = []
    for r in record:
        comm = r.split()
        if comm[0] == 'Enter':
            userInfo[comm[1]] = comm[2]
            logs.append((comm[1],"님이 들어왔습니다."))
        elif comm[0] == 'Leave':
            logs.append((comm[1],"님이 나갔습니다."))
        else:
            userInfo[comm[1]] = comm[2]
    return list(map(lambda x : userInfo[x[0]] + x[1],logs))

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))