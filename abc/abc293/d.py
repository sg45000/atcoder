"""
Union Find Treeで解く
treeで繋がりを管理すると、rootになっている頂点の数だけロープの組みが存在する (x + y)
各ロープについて、どちらかがつながっていなければその組は環状ではない
それ以外は環状
"""

class UnionFindTree():
    def __init__(self, n: int):
        self.__parents = [i for i in range(n)]
        self.__ranks = [0] * n  # 木の高さ

    def find_root(self, x: int):
        if x != self.__parents[x]:
            self.__parents[x] = self.find_root(self.__parents[x])
        return self.__parents[x]
    
    def unite(self, x: int, y: int):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        if self.__ranks[x] > self.__ranks[y]:
            self.__parents[y] = x
        else:
            self.__parents[x] = y
            if self.__ranks[x] == self.__ranks[y]:
                self.__ranks[y] += 1

    def is_same(self, x: int, y: int):
        x = self.find_root(x)
        y = self.find_root(y)
        return x == y


N, M = list(map(int, input().split(" ")))

tree = UnionFindTree(N)

G = [(None, None)] * N
for _ in range(M):
    a, b, c, d = input().split(" ")
    a, b, c, d = int(a) - 1, b, int(c) - 1, d
    tree.unite(a, c)
    if b == 'B':
        G[a] = (c, G[a][1])
    else:
        G[a] = (G[a][0], c)
    if d == 'B':
        G[c] = (a, G[c][1])
    else:
        G[c] = (G[c][0], a)

x, y = 0, 0
k = [0] * N
for i in range(N):
    b, r = G[i]
    if b is None or r is None:
        k[tree.find_root(i)] = -1

for i in range(N):
    b, r = G[i]
    if k[tree.find_root(i)] >= 0:
        k[tree.find_root(i)] = 1

for a in k:
    if a == 1:
        x += 1
    elif a == -1:
        y += 1
    
print(x, y)