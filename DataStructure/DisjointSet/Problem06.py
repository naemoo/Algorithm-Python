# https://www.acmicpc.net/problem/4195
import sys
from collections import defaultdict

read = sys.stdin.readline
test = int(read().strip())


def friend_to_idx(p, q):
    if not (p in friend_idx.keys()):
        friend_idx[p] = len(friend_idx)
    if not (q in friend_idx.keys()):
        friend_idx[q] = len(friend_idx)
    return friend_idx[p], friend_idx[q]


def find(idx):
    if tree[idx][0] == idx:
        return idx
    tree[idx][0] = find(tree[idx][0])
    return tree[idx][0]


def merge(p, q):
    if tree[p][1] > tree[q][1]:
        tree[q][0] = p
    elif tree[p][1] < tree[q][1]:
        tree[q][0] = p
    else:
        tree[p][1] += 1
        tree[q][0] = p


while test:
    f = int(read().strip())
    net_cnt = defaultdict(lambda : 1)
    friend_idx = dict()
    networks = []
    while f:
        p, q = friend_to_idx(*(read().strip().split()))
        networks.append((p, q))
        f -= 1
    tree = [[i, 0] for i in range(len(friend_idx))]
    for p, q in networks:
        p, q = find(p), find(q)
        if p != q:
            merge(p, q)
            p = find(p)
            net_cnt[p] += net_cnt[q]
        print(net_cnt[p])
    test -= 1
