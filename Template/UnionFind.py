class UnionFind(object):
    class Node(object):
        def __init__(self, parent):
            self.parent = parent
            self.depth = 0

        def __repr__(self):
            return "({},{})".format(self.parent,self.depth)

    def find(self, i):
        if self.nodes[i].parent != i:
            self.nodes[i].parent = self.find(self.nodes[i].parent)
        return self.nodes[i].parent

    def merge(self, p, q):
        p, q = self.find(p), self.find(q)
        if self.nodes[p].depth == self.nodes[q].depth:
            self.nodes[p].depth += 1
            self.nodes[q].parent = p
        elif self.nodes[p].depth < self.nodes[q].depth:
            self.nodes[p].parent = q
        else:
            self.nodes[q].parent = p

    def __init__(self, n):
        self.n = n
        self.nodes = [self.Node(e) for e in range(n)]

    def __str__(self):
        return str(self.nodes)
