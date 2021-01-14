# https://www.acmicpc.net/problem/1713
import sys

read = sys.stdin.readline
n = int(read().strip())
read().strip()
candidates = list(map(int, read().strip().split()))
counter = dict()

seq = 0
for candidate in candidates:
    if candidate in counter.keys():
        counter[candidate][0] += 1
    else:
        if seq < n:
            counter[candidate] = [1, seq]
            seq += 1
        else:
            idx = sorted(counter.items(), key=lambda x: x[1])[0][0]
            counter.pop(idx)
            seq += 1
            counter[candidate] = [1, seq]

for e in sorted(counter.keys()):
    print(e, end=' ')
