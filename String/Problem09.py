# https://www.acmicpc.net/problem/9202
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline
n = int(read().strip())
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
scores = (0, 0, 0, 1, 1, 2, 3, 5, 11)


class Node(object):
    def __init__(self):
        self.isEnd = False
        self.child = defaultdict(Node)


class Tries(object):
    def __init__(self):
        self.head = Node()

    def add(self, word):
        cur = self.head
        for c in word:
            cur = cur.child[c]
        cur.isEnd = True

    def isContain(self, word):
        cur = self.head
        for c in word:
            if c in cur.child.keys():
                cur = cur.child[c]
            else:
                return False
        return True

    def isWord(self, word):
        cur = self.head
        for c in word:
            if c in cur.child.keys():
                cur = cur.child[c]
            else:
                return False
        return True if cur.isEnd else False


dictionary = Tries()
for _ in range(n):
    dictionary.add(read().strip())

read().strip()
t = int(read().strip())


def dfs(x, y, cw):
    if not visit[x][y] or len(cw) > 8:
        return
    visit[x][y] = False
    if dictionary.isWord(cw):
        finds.add(cw)

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if visit[nx][ny]:
                nw = cw + borads[nx][ny]
                if dictionary.isContain(nw):
                    dfs(nx, ny, nw)
    visit[x][y] = True


while t:
    borads = [read().strip() for _ in range(4)]
    finds = set()
    for i in range(4):
        for j in range(4):
            visit = [[True for _ in range(4)] for _ in range(4)]
            dfs(i, j, borads[i][j])

    score = 0
    for word in finds:
        score += scores[len(word)]

    print(score, sorted(finds, key=lambda x: (-len(x), x))[0], len(finds))
    read().strip()
    t -= 1
