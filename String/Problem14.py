# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    return sum(map(lambda x: absolutes[x[0]], filter(lambda x: x[1], enumerate(signs)))) - sum(
        map(lambda x: absolutes[x[0]], filter(lambda x: not x[1], enumerate(signs))))


solution([4, 7, 12], [True, False, True])
