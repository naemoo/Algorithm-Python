# https://programmers.co.kr/learn/courses/30/lessons/60061
bo = 1
pil = 0
frames = set()

def solution(n, build_frame):
    for x, y, a, b in build_frame:
        if b:
            if can_put(x, y, a):
                frames.add((x, y, a))
        else:
            frames.remove((x, y, a))
            for frame in frames:
                if not can_put(*frame):
                    frames.add((x, y, a))
                    break
    return sorted(frames)


def can_put(x, y, a):
    if a == pil:
        if y == 0:
            return True
        elif (x - 1, y, bo) in frames or (x, y, bo) in frames:
            return True
        elif (x, y - 1, pil) in frames:
            return True
    else:
        if (x, y - 1, pil) in frames or (x + 1, y - 1, pil) in frames:
            return True
        elif (x - 1, y, bo) in frames and (x + 1, y, bo) in frames:
            return True
    return False

