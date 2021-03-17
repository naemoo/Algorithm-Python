def solution(purchase):
    months = dict(zip(range(1, 13), (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)))
    ans = [0] * 5
    arr = [0 for _ in range(400)]

    def month_to_day(month):
        month, day = map(int, month.split('/')[1:])
        ret = 0
        for i in range(1, month):
            ret += months[i]
        ret += (day - 1)
        return ret

    for log in purchase:
        year, cost = log.split()
        day, cost = month_to_day(year), int(cost)
        arr[day] += cost
        arr[day + 30] -= cost

    prefix = [0 for _ in range(400)]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    for e in prefix[1:366]:
        if e < 10000:
            ans[0] += 1
        elif 10000 <= e < 20000:
            ans[1] += 1
        elif 20000 <= e < 50000:
            ans[2] += 1
        elif 50000 <= e < 100000:
            ans[3] += 1
        else:
            ans[4] += 1
    return ans


ans = solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"])
print(ans)
ans = solution(
    ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"])
print(ans)
