# https://www.acmicpc.net/problem/5052
import sys
from collections import defaultdict

class Node(object):
    def __init__(self):
        self.isEnd = False
        self.child = defaultdict(Node)

class Tries(object):
    def __init__(self):
        self.head = Node()

    def add(self,word):
        cur = self.head
        for c in word:
            cur = cur.child[c]
            if cur.isEnd:
                return False
        cur.isEnd = True
        return True

    def find(self,word):
        cur = self.head
        for c in word:
            cur = cur.child[c]
        return cur.isEnd

read = sys.stdin.readline
t = int(read().strip())
for _ in range(t):
    n = int(read().strip())
    words = []
    for _ in range(n):
        words.append(read().strip())
    words = sorted(words,key=lambda x : len(x))

    flag = True
    tries = Tries()
    for word in words:
        if not tries.add(word):
            print("NO")
            flag = False
            break
    if flag:
        print("YES")