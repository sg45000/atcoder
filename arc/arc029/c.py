"""
i番目の都市に公益所を設置するかどうか
ある仮想の都市xがあると想定して、i番目の都市とxを結ぶ道のコストを公益所を設置するコストと言い換えることができる
つまり、都市xとそれぞれにつながる道を仮想的に設置した状態で最小全域木を求める問題。
クラスカル法で答えを求めることができる
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


roads = []

for i in range(1, N + 1):
    c = int(input())
    roads.append((0, i, c))

for i in range(M):
    a, b, r = list(map(int, input().split(" ")))
    roads.append((a, b, r))

roads.sort(key=lambda x: x[2])

tree = UnionFindTree(N + 1)

ans = 0
for a, b, r in roads:
    if not tree.is_same(a, b):
        tree.unite(a, b)
        ans += r

print(ans)