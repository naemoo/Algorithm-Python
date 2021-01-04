# https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3
import sys
sys.setrecursionlimit(2*(10**5))
class UnionFind(object):
    def find(self, i):
        if not i in self.nodes.keys():
            self.nodes[i] = i

        if self.nodes[i] != i:
            self.nodes[i] = self.find(self.nodes[i])
        return self.nodes[i]

    def merge(self, p, q):
        p, q = self.find(p), self.find(q)
        if p != q:
            if p >= q:
                self.nodes[q] = p
            else:
                self.nodes[p] = q

    def __init__(self):
        self.nodes = dict()

def solution(k, room_number):
    hotel = UnionFind()
    ans = []
    for room in room_number:
        av = hotel.find(room)
        ans.append(av)
        hotel.merge(hotel.find(av + 1), av)
    return ans

print(solution(10, [1, 3, 4, 1, 3, 1]))
