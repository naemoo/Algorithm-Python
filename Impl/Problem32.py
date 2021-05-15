# https://programmers.co.kr/learn/courses/30/lessons/49994
directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}


def solution(dirs):
    x, y = (0, 0)
    visit = set()
    for d in dirs:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue

        e = ((x, y), (nx, ny))
        visit.add(tuple(sorted(e)))
        x, y = nx, ny
    return len(visit)


solution("ULURRDLLU")
solution("LULLLLLLU")
