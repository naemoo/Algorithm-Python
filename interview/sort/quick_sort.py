def partition(arr, l, r):
    pivot = arr[l]
    left, right = l, r
    while left < right:
        while arr[right] > pivot:
            right -= 1
        while right > left and arr[left] <= pivot:
            left += 1

        arr[left], arr[right] = arr[right], arr[left]

    arr[left], arr[l] = arr[l], arr[left]
    return right


def quickSort(arr, l, r):
    if l >= r:
        return

    pivot = partition(arr, l, r)

    quickSort(arr, l, pivot - 1)
    quickSort(arr, pivot + 1, r)


tmp = [30, 70, 40, 20, 10, 50, 80]
quickSort(tmp, 0, len(tmp) - 1)
print(tmp)
