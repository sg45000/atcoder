N, Q = list(map(int, input().split(" ")))

class UnionFindTree():
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n  # 木の高さ

    def find_root(self, x: int):
        if x != self.parents[x]:
            self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]
    
    def unite(self, x: int, y: int):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        if self.ranks[x] > self.ranks[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.ranks[x] == self.ranks[y]:
                self.ranks[y] += 1

    def is_same(self, x: int, y: int):
        x = self.find_root(x)
        y = self.find_root(y)
        return x == y


tree = UnionFindTree(N)
for _ in range(Q):
    P, A, B = list(map(int, input().split(" ")))
    if P == 0:
        tree.unite(A, B)
    else:
        if tree.is_same(A, B):
            print("Yes")
        else:
            print("No")