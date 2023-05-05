# union find木
class UnionFind:
    def __init__(self, h, w) -> None:
        self.parent = dict()
        self.rank = dict()
        for i in range(w):
            for j in range(h):
                self.parent[(i, j)] = (i, j)
                self.rank[(i, j)] = 0

    def root(self, position):
        if self.parent[position] == position:
            return position
        self.parent[position] = self.root(self.parent[position])
        return self.parent[position]

    def unite(self, u, v):
        ur = self.root(u)
        vr = self.root(v)
        if ur == vr:
            return
        if self.rank[ur] < self.rank[vr]:
            ur, vr = vr, ur
        self.rank[ur] += 1
        self.parent[vr] = ur

    def same(self, u, v):
        return self.root(u) == self.root(v)


H, W = list(map(int, input().split(" ")))
Q = int(input())

grid = [[0] * H for _ in range(W)]
uf = UnionFind(H, W)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(Q):
    q = list(map(int, input().split(" ")))
    if q[0] == 1:
        r = q[1] - 1
        c = q[2] - 1
        grid[c][r] = 1
        for x, y in zip(dx, dy):
            nr = r + y
            nc = c + x
            if 0 <= nr < H and 0 <= nc < W and grid[nc][nr] == 1:
                uf.unite((nc, nr), (c, r))
    else:
        ra = q[1] - 1
        ca = q[2] - 1
        rb = q[3] - 1
        cb = q[4] - 1
        if grid[ca][ra] == 1 and grid[cb][rb] == 1 and uf.same((ca, ra), (cb, rb)):
            print("Yes")
        else:
            print("No")
