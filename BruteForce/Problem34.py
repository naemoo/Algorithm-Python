# https://www.acmicpc.net/problem/1525
import sys
from collections import defaultdict, deque

read = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
init = ''.join(map(lambda x: ''.join(x), [read().strip().split() for _ in range(3)]))
visit = defaultdict(int)
visit[init] = 0

q = deque([init])
while q:
    word = q.popleft()

    cur = word.find('0')
    x, y = cur // 3, cur % 3
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue
        nxt = 3 * nx + ny
        nxt_word = list(word)
        nxt_word[cur], nxt_word[nxt] = nxt_word[nxt], nxt_word[cur]
        nxt_word = ''.join(nxt_word)
        if nxt_word in visit.keys():
            continue

        q.append(nxt_word)
        visit[nxt_word] = visit[word] + 1

print(visit['123456780'] if '123456780' in visit.keys() else -1)
