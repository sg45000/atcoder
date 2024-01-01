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


############   回答   ###########
"""
逆からUnionFind
"""

N, M = list(map(int, input().split(" ")))
AB = [list(map(int, input().split(" "))) for _ in range(M)]

tree = UnionFindTree(N)

G = [[] for _ in range(N)]

for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 0
ans_list = [0]
active = [False] * N  # 復活した頂点を管理
for u in reversed(range(1, N)):
    active[u] = True
    ans += 1
    for v in G[u]:
        if active[v] and not tree.is_same(v, u):
            ans -= 1
            tree.unite(v, u)
    ans_list.append(ans)

for a in ans_list[::-1]:
    print(a)