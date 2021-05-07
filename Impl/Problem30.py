# https://programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    board = list(map(list, board))
    board = list(map(lambda x: list(x), zip(*board)))
    for e in board:
        e.reverse()
    flag = True
    
    while flag:
        flag = False
        erases = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n - 1):
            for j in range(m - 1):
                tmp = set()
                for x in range(2):
                    for y in range(2):
                        tmp.add(board[i + x][j + y])
                if len(tmp) == 1 and not 0 in tmp:
                    flag = True
                    for x in range(2):
                        for y in range(2):
                            erases[i + x][j + y] = True

        for i in range(n):
            for j in range(m - 1, -1, -1):
                if erases[i][j]:
                    board[i].pop(j)
                    board[i].append(0)

    return sum(map(lambda x: len(list(filter(lambda y: y == 0, x))), board))


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
