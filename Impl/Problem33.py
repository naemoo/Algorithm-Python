# https://programmers.co.kr/learn/courses/30/lessons/77484#fn1
def solution(lottos, win_nums):
    not_zeros = list(filter(lambda x: x != 0, lottos))
    cnt = 0
    for not_zero in not_zeros:
        if not_zero in win_nums:
            cnt += 1
    getRank = lambda cnt: 7 - cnt if cnt >= 2 else 6
    return [getRank(cnt + 6 - len(not_zeros)), getRank(cnt)]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
