# https://www.acmicpc.net/problem/2212
import sys

read = sys.stdin.readline
n = int(read().strip())
k = int(read().strip())
sensors = list(map(int, read().strip().split()))
sensors.sort()
sensors_lens = []
for i in range(n - 1):
    sensors_lens.append(sensors[i + 1] - sensors[i])

sensors_lens.sort()

k -= 1
while sensors_lens and k:
    sensors_lens.pop()
    k -= 1

print(sum(sensors_lens))
