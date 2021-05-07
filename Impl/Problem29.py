# https://programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    dictionary = dict(zip(map(chr, range(ord('A'), ord('Z') + 1)), range(1, 27)))
    ans = []
    w = 0
    while w < len(msg):
        c = w
        tmp = msg[w]
        isLast = False
        while c < len(msg) and (tmp in dictionary.keys()):
            c += 1
            if c < len(msg):
                tmp += msg[c]
            else:
                isLast = True
        if isLast:
            ans.append(dictionary[tmp])
        else:
            ans.append(dictionary[tmp[:-1]])
        dictionary[tmp] = len(dictionary) + 1
        w = c

    return ans


# print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
