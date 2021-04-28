# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    arr = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    ans = []
    for e in queries:
        lx, ly, rx, ry = map(lambda x: x - 1, e)
        seq = (ry - ly + 1, rx - lx, ry - ly, rx - lx - 1)
        tmp = []
        for i, s in enumerate(seq):
            if i == 0:
                for j in range(s):
                    tmp.append(arr[lx][ly + j])
            elif i == 1:
                for j in range(1, s + 1):
                    tmp.append(arr[lx + j][ry])
            elif i == 2:
                for j in range(1, s + 1):
                    tmp.append(arr[rx][ry - j])
            else:
                for j in range(1, s + 1):
                    tmp.append(arr[rx - j][ly])
        tmp.insert(0, tmp.pop())
        cnt = 0
        for i, s in enumerate(seq):
            if i == 0:
                for j in range(s):
                    arr[lx][ly + j] = tmp[cnt]
                    cnt += 1
            elif i == 1:
                for j in range(1, s + 1):
                    arr[lx + j][ry] = tmp[cnt]
                    cnt += 1
            elif i == 2:
                for j in range(1, s + 1):
                    arr[rx][ry - j] = tmp[cnt]
                    cnt += 1
            else:
                for j in range(1, s + 1):
                    arr[rx - j][ly] = tmp[cnt]
                    cnt += 1
        ans.append(min(tmp))

    return ans


ans = solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
print(ans)
ans = solution(100, 97, [[1, 1, 100, 97]])
print(ans)
