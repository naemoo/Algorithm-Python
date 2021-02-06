# https://www.acmicpc.net/problem/1837
import sys

read = sys.stdin.readline
n, k = read().strip().split()


def getPrime(k):
    k = int(k)
    visit = [False for _ in range(k)]
    visit[0] = visit[1] = True
    for i in range(2, k):
        if visit[i]:
            continue
        for j in range(i * 2, k, i):
            visit[j] = True
    return list(filter(lambda x: not visit[x], range(k)))


primes = getPrime(k)


for prime in primes:
    plen = len(str(prime))
    tmp = ''
    for e in n:
        tmp += e
        if int(tmp) < prime:
            continue
        tmp = str(int(tmp) % prime)
    if tmp == '0':
        print("BAD", prime)
        sys.exit()
print("GOOD")
