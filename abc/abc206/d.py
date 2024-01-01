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

N = int(input())
A = list(map(int, input().split(" ")))

tree = UnionFindTree(max(A) + 1)


for i in range(N // 2):
    if A[i] != A[N - 1 - i]:
        tree.unite(A[i], A[N - 1 - i])

C = [0] * (max(A) + 1)
for i in range(1, max(A) + 1):
    C[tree.find_root(i)] += 1

ans = 0
for a in C:
    if a > 0:
        ans += a - 1

print(ans)