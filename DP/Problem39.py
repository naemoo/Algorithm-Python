# https://programmers.co.kr/learn/courses/30/lessons/1843
def solution(arr):
    nums = list(map(int, arr[:len(arr):2]))
    ops = arr[1:len(arr):2]
    n = len(nums)
    dp = [[None for _ in range(102)] for _ in range(102)]

    def getMax(st, to):
        if to - st == 1:
            if ops[st] == '+':
                tmp = nums[to] + nums[st]
                dp[st][to] = [tmp, tmp]
                return dp[st][to]
            else:
                tmp = nums[st] - nums[to]
                dp[st][to] = [tmp, tmp]
                return dp[st][to]
        elif st == to:
            dp[st][to] = [nums[st], nums[st]]
            return dp[st][to]

        if dp[st][to] != None:
            return dp[st][to]
        ret_max = -float('inf')
        ret_min = float('inf')
        for k in range(st, to):
            if ops[k] == '+':
                tmp_max = max(getMax(st, k)) + max(getMax(k + 1, to))
                tmp_min = min(getMax(st, k)) + min(getMax(k + 1, to))
                ret_max = max(ret_max, tmp_max)
                ret_min = min(ret_min, tmp_min)
            else:
                tmp_max = max(getMax(st, k)) - min(getMax(k + 1, to))
                tmp_min = min(getMax(st, k)) - max(getMax(k + 1, to))
                ret_max = max(ret_max, tmp_max)
                ret_min = min(ret_min, tmp_min)
        dp[st][to] = (ret_max, ret_min)
        return dp[st][to]

    return max(getMax(0, n - 1))


ans = solution(["1", "-", "3", "+", "5", "-", "8"])
print(ans)
