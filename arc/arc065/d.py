from collections import defaultdict


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
    

N, K, L = list(map(int, input().split(" ")))

road = UnionFindTree(N)
for _ in range(K):
    p, q = list(map(int, input().split(" ")))
    road.unite(p - 1, q - 1)

train = UnionFindTree(N)
for _ in range(L):
    r, s = list(map(int, input().split(" ")))
    train.unite(r - 1, s - 1)

# 道路と電車が両方つながっているかは、任意の2都市のrootがそれぞれ同じかで判定できる
d = defaultdict(int)
for i in range(N):
    d[(road.find_root(i), train.find_root(i))] += 1

for i in range(N):
    print(d[(road.find_root(i), train.find_root(i))])