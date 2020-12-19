# https://www.acmicpc.net/problem/1644
def getPrimes(num):
    arr = [i for i in range(num+1)]
    arr[1] = 0

    for e in arr:
        if e == 0:
            continue
        for j in range(e*2,num+1,e):
            arr[j] = 0
    return list(filter(lambda x : x != 0, arr))
n = int(input())
primes = getPrimes(n)
end,sum,ans = 0,0,0

for start in range(len(primes)):
    while sum < n and end < len(primes):
        sum += primes[end]
        end += 1

    if sum == n:
        ans += 1

    sum -= primes[start]
print(ans)
