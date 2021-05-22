def insert_sort(arr):
    for i in range(1, len(arr)):
        # 새로운 값과 비교
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(arr)


insert_sort([2, 1, 0, 3, 4])
