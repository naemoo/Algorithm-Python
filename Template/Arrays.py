#%%
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#%% 대각선 기준 뒤집기
def reverse(arr):
    return list(map(list,zip(*arr)))
print(reverse(arr))
# %% 시계방향 회전
def rotate(arr):
    arr.reverse()
    return list(map(list,zip(*arr)))
print(rotate(arr))
# %% 반시계 방향 회전
def unRotate(arr):
    for r in arr:
        r.reverse()
    return list(map(list,zip(*arr)))    
print(unRotate(arr))
# %% nxn 배열에서 m 만큼 zero padding
def padding(arr,m):
    n = len(arr)
    size = 2*m + n
    padArr = [[0] * size for _ in range(size)]

    for i in range(m,m+n):
        for j in range(m,m+n):
            padArr[i][j] = arr[i-m][j-m]
    return padArr
# %%

