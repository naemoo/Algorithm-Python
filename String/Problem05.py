# %% https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def solution(n, arr1, arr2):
    return ["".join(map(lambda x : '#' if x=='1' else ' ', format(a|b,'b').zfill(n))) for a,b in zip(arr1,arr2)]
# %%
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
