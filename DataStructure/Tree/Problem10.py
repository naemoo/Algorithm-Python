# https://www.acmicpc.net/problem/5639
import sys
from collections import defaultdict
sys.setrecursionlimit(10001)

class Node(object):
    def __init__(self):
        self.num = None
        self.left = None
        self.right = None

tree = defaultdict(Node)

read = sys.stdin.readline
n = int(read().strip())
head = None

try:
    while 1:
        if not head:
            head = n
        cur = tree[head]
        while cur:
            if cur.num == None:
                cur.num = n
                cur.left = Node()
                cur.right = Node()
                break
            elif cur.num >= n:
                cur = cur.left
            else:
                cur = cur.right
        n = int(read().strip())
except:
    pass


def postOrder(cur):
    if cur.num == None:
        return
    postOrder(cur.left)
    postOrder(cur.right)
    print(cur.num)


postOrder(tree[head])
