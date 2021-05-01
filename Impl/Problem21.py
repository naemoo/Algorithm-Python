# https://programmers.co.kr/learn/courses/30/lessons/42894

def solution(board):
    ans = 0

    def isSquare(x, y, r, c):
        z_cnt = 0
        tmp = 0
        if x + r > len(board) or y + c > len(board):
            return False

        for i in range(x, x + r):
            for j in range(y, y + c):
                if board[i][j] == 0:
                    z_cnt += 1
                else:
                    if tmp == 0:
                        tmp = board[i][j]
                    elif board[i][j] != tmp:
                        return False
        return z_cnt == 2

    def canPut(x, y, r, c):
        z_cnt = 0
        for j in range(y, y + c):
            flag = False
            for i in range(x):
                if board[i][j]:
                    flag = True
                    break
            if flag:
                continue
            for i in range(x, x + r):
                if board[i][j]:
                    break
                z_cnt += 1
        return z_cnt == 2

    def fill_zero(x, y, r, c):
        for i in range(x, x + r):
            for j in range(y, y + c):
                board[i][j] = 0

    i, j = 0, 0
    while i < len(board):
        j = 0
        while j < len(board):
            if isSquare(i, j, 2, 3):
                if canPut(i, j, 2, 3):
                    ans += 1
                    fill_zero(i, j, 2, 3)
                    i, j = 0, 0

            if isSquare(i, j, 3, 2):
                if canPut(i, j, 3, 2):
                    ans += 1
                    fill_zero(i, j, 3, 2)
                    i, j = 0, 0
            j += 1
        i += 1
    return ans


solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
          [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
          [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]])
solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             , [0, 0, 0, 2, 2, 0, 0, 0, 0, 0]
             , [0, 0, 0, 2, 1, 0, 0, 0, 0, 0]
             , [0, 0, 0, 2, 1, 0, 0, 0, 0, 0]
             , [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
             , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
