def solution(n):
    arr = [ i for i in range(n+1)]
    arr[1] = 0

    for e in arr:
        if e == 0:
            continue
        for j in range(e*2,n+1,e):
            arr[j] = 0

    return len(list(filter(lambda x : x != 0, arr)))

print(solution(10))
