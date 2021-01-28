# https://www.acmicpc.net/problem/1991
import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read().strip())
head = None


class Node:
    def __init__(self):
        self.left = None
        self.right = None


tree = defaultdict(Node)

for _ in range(n):
    node, l, r = read().strip().split()
    if not head:
        head = node
    tree[node].left = l
    tree[node].right = r


def preOrder(cur):
    if cur == '.':
        return
    print(cur, end='')
    preOrder(tree[cur].left)
    preOrder(tree[cur].right)


def inOrder(cur):
    if cur == '.':
        return
    inOrder(tree[cur].left)
    print(cur, end='')
    inOrder(tree[cur].right)





preOrder(head)
print()
inOrder(head)
print()
postOrder(head)
