from cmath import sqrt
from functools import reduce
from typing import Callable, Generic, List, Set, Tuple, TypeVar
from itertools import chain, count, permutations
from collections import defaultdict, deque
from statistics import median_low
import sys

sys.setrecursionlimit(10**9)

T = TypeVar("T")

#############################
# input
#############################

get_ints = lambda: list(map(int, input().split()))
get_ints_n_lines = lambda n: [list(map(int, input().split())) for _ in range(n)]

get_chars = lambda: list(input())
get_chars_with_trim = lambda s: list(input().split(s))

#############################
# Functional
#############################


def identify(x: T) -> T:
    return x


#############################
# List
#############################


class FlexibleList(Generic[T], list):
    begin: int
    end: int

    def __init__(self, initial_data=None, initial_range: (int, int) = None):
        if initial_data is None:
            initial_data = []
        super().__init__(initial_data)
        if initial_range is None:
            self.begin = 0
            self.end = len(self)
        else:
            self.begin = initial_range[0]
            self.end = initial_range[1]

    def __getitem__(self, index):
        if index < self.begin or self.end < index:
            raise IndexError("Index out of range")
        if isinstance(index, int):
            index -= self.begin
        return super().__getitem__(index)


#############################
# Grid
#############################


Coordinate = Tuple[int, int]


def get_char_grid(
    upper_left: Coordinate, lower_right: Coordinate, trim_string: str | None
) -> FlexibleList[FlexibleList[int]]:
    """_summary_
    文字で構成されたグリッドを読み込み2次元配列で返す
    """
    (ulh, ulw) = upper_left
    (lrh, lrw) = lower_right
    return FlexibleList(
        [
            FlexibleList(
                get_chars_with_trim(trim_string) if trim_string else get_chars(),
                (ulw, lrw),
            )
            for _ in range(lrh + 1 - ulh)
        ],
        (ulh, lrh),
    )


def range_to_coords(
    upper_left: Coordinate, lower_right: Coordinate
) -> List[Coordinate]:
    """_summary_
    指定した矩形内の座標を全て返す
    """
    (sh, sw) = upper_left
    (gh, gw) = lower_right
    ar = []
    for i in range(sh, gh + 1):
        for j in range(sw, gw + 1):
            ar.append((i, j))
    return ar


def in_range(
    upper_left: Coordinate, lower_right: Coordinate, target: Coordinate
) -> bool:
    """_summary_
    指定した指定した矩形内の座標にtargetが含まれているかをチェックする
    """
    (sh, sw) = upper_left
    (gh, gw) = lower_right
    (th, tw) = target
    return sh <= th <= gh and sw <= tw <= gw


def linear_scan_n(
    grid: FlexibleList[FlexibleList[T]], n: int, d: (int, int), s: (int, int)
) -> List[T] | None:
    """_summary_
    gridの指定した数だけ直線に切り取る
    gridの範囲を超えた場合Noneを返す
    """
    ret = []
    for _ in range(n):
        try:
            ret.append(grid[s[0]][s[1]])
            s = tuple([a + b for a, b in zip(d, s)])
        except IndexError:
            return None
    return ret


def rotate(coord: Coordinate, n: int) -> Coordinate:
    """
    正方形を前提として時計回りに90度回転
    """
    i, j = coord
    return (j, n + 1 - i)


def vertical_dist():
    """
    水平垂直方向の移動
    """
    return [(1, 0), (0, 1), (-1, 0), (0, -1)]


def diagonal_dist():
    """
    斜め方向の移動
    """
    return [(1, 1), (-1, -1), (-1, 1), (1, -1)]


def ixmap(v: Tuple[int, int], h: int, w: int) -> Tuple[int, int]:
    i, j = v
    return (i % h, j % w)


def next_in_grid_range(
    grid: FlexibleList[FlexibleList[T]], s: Tuple[int, int], dist: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    s地点からdist方向へ移動した場合の地点を返す。gridの範囲を超えた地点は返さない
    """
    sh, sw = s
    nexts = [(sh + h, sw + w) for h, w in dist]
    return [
        (h, w)
        for h, w in nexts
        if grid.begin <= h <= grid.end and grid[0].begin <= w <= grid[0].end
    ]


#############################
# GridSet
#############################

GridSet = Set[Coordinate]


def to_gs(coords: List[Coordinate]) -> GridSet:
    return set(coords)


def from_grid_gs(f, grid: FlexibleList[FlexibleList[T]]) -> GridSet:
    ret = []
    for i in range(grid.begin, grid.end + 1):
        for j in range(grid[i].begin, grid[i].end + 1):
            if f(grid[i][j]):
                ret.append((i, j))
    return set(ret)


def rotates_gs(coords: GridSet, n: int) -> GridSet:
    """
    正方形を前提としてGridSetを90度回転
    """
    return set(rotate(coord, n) for coord in coords)


def is_shifted_gs(s1: GridSet, s2: GridSet) -> bool:
    """
    2つのGridSetを縦横の並行移動した時に同じ形になるか
    """
    if len(s1) != len(s2):
        return False
    if len(s1) == len(s2) == 0:
        return True
    return all(a == b for a, b in zip(normalize_gs(s1), normalize_gs(s2)))


def is_contain_gs(s1: GridSet, s2: GridSet) -> bool:
    """
    s1がs2に含まれているか
    """
    return len(s1.difference(s2)) == 0


def normalize_gs(coords: GridSet) -> GridSet:
    """
    GridSetの座標を正規化((0,0)の原点を基準に)する
    """
    i, j = min(coords)
    return set(sorted([(u - i + 1, v - j + 1) for u, v in coords]))


def extract_from_extended_gs(
    upper_left: Coordinate, lower_right: Coordinate, h: int, w: int, gs: GridSet
) -> GridSet:
    """
    縦横に無限に拡張したGridから指定した範囲を切り取る
    0-indexグリッドを前提とする
    """
    ret = set()
    for i, j in range_to_coords(upper_left, lower_right):
        if (i % h, j % w) in gs:
            ret.add((i, j))
    return ret


def linear_scan_n_gs(
    gs: GridSet, n: int, d: (int, int), s: (int, int)
) -> GridSet | None:
    """_summary_
    gridの指定した数だけ直線に切り取る
    gridの範囲を超えた場合Noneを返す
    """
    ret = set()
    for _ in range(n):
        if s in gs:
            ret.add(s)
            s = tuple([a + b for a, b in zip(d, s)])
        else:
            return None
    return ret


#############################
# BIT (Binary Index Tree)
#############################


class BIT:
    """
    https://output-zakki.com/binary_indexed_tree/
    """

    def __init__(self, n: int):
        self._size = n
        self._tree = [0] * (n + 1)  # 1-index

    def add(self, i: int, x: int):
        while i <= self._size:
            self._tree[i] += x
            i += i & -i

    def sum(self, i: int):
        total = 0
        while i > 0:
            total += self._tree[i]
            i -= i & -i
        return total


#############################
# 転倒数
#############################


def inversion_number(xs: List[int]):
    """
    転倒数の計算 (1-indexを前提とする)
    O(N log N)
    """
    num = 0
    bit = BIT(len(xs))
    for i in range(len(xs)):
        num += i - bit.sum(xs[i])  # num += 現時点でbitに移動した個数 - i番目の数値より小さい数値の個数
        bit.add(xs[i], 1)

    return num


#############################
# 進数変換
#############################


def fromDigits(base: int, x: int):
    """
    N進数から10進数に変換する
    """
    xs = [int(digit) for digit in str(x)]
    s = 0
    for i in range(len(xs)):
        s += xs[-i - 1] * base**i
    return s


def toDigits(base: int, x: int):
    """
    10進数からN進数に変換する
    """
    if x == 0:
        return 0
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    digits.reverse()
    return int("".join(digits))


#############################
# DAG
#############################


def topological_sort(V: int, G: List[List[int]], indeg: List[int]) -> List[int]:
    """
    DAGのトポロジカルソートを行い、順序付けられた頂点のリストを返します。
    V: 頂点数
    G: DAGのグラフ
    indeg: 各頂点の入次数
    """
    indeg = indeg.copy()
    q = deque()

    # 1.入次数0の頂点を発見し、キューに追加
    for i in range(V):
        if indeg[i] == 0:
            q.append(i)

    sorted_list = []
    while q:
        v = q.popleft()
        sorted_list.append(v)  # キューの中の頂点は入次数が0の頂点なのでリストに追加

        for adj in G[v]:
            indeg[adj] -= 1  # 2. 入次数0の頂点から到達できる頂点の入次数を1減らす
            if indeg[adj] == 0:
                q.append(adj)  # 入次数0になったらキューに追加
    return sorted_list


def is_DAG(V: int, G: List[List[int]], indeg: List[int]):
    """
    与えられたグラフがDAG（Directed Acyclic Graph）であるかどうかを判断します。
    V: 頂点数
    G: グラフの隣接リスト表現
    indeg: 各頂点の入次数のリスト
    """
    sorted_list = topological_sort(V, G, indeg)
    return len(sorted_list) == V


#############################
# UnionFindTree
#############################


class UnionFindTree:
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


#############################
# BFS
#############################
Graph = List[List[int]]


def get_undirected_graph(n: int) -> Graph:
    """
    0-indexで無向グラフを入力から取得する
    """
    G: Graph = [[] for _ in range(n)]
    i, j = get_ints()
    G[i - 1].append(j - 1)
    G[j - 1].append(i - 1)
    return G


def bfs(
    n: int, s: int, g: Graph, unit: int, operation: Callable[[int], int]
) -> List[int]:
    """
    n: ノード総数
    s: 最初に探索するノード
    g: グラフ
    """

    q = deque()
    q.append(s)
    visited = [unit] * n

    while q:
        v = s.popleft()
        for nex in g[v]:
            if unit != visited[nex]:
                continue
            visited[nex] = operation(visited[v])
            q.append(nex)

    return visited


#############################
# 組み合わせ数
#############################


def ncr_mod(n, r, mod):
    """
    組合せを求める 素数で割ったあまりを求める時に使う
    n = 全数
    r = 何個選ぶか
    p = 法
    計算量: O(r)"""
    ret = 1
    for i in range(1, r + 1):
        ret = (ret * (n - i + 1) * pow(i, mod - 2, mod)) % mod
    return ret


def dup_comb_mod(n, r, p):
    """
    重複組合せを求める 素数で割ったあまりを求める時に使う
    n = 種類数
    r = 重複を許して何個選ぶか
    p = 法
    計算量: O(n)"""
    fact = [1] * (n + 5)  # iの階乗をpで割ったあまり
    fact_inv = [1] * (n + 5)  # factの逆元
    inv = [1] * (n + 5)  # iの逆元

    fact[0] = fact[1] = 1
    fact_inv[0] = fact_inv[1] = 1
    inv[1] = 1

    for i in range(2, n + 5):
        fact[i] = fact[i - 1] * i % p
        inv[i] = p - inv[p % i] * (p // i) % p
        fact_inv[i] = fact_inv[i - 1] * inv[i] % p
    return fact[n] * ((fact_inv[r] * fact_inv[n - r]) % p) % p


#############################
# マンハッタン距離
#############################


# 座標を45°回転
def to_manhattan_coord(xy) -> Coordinate:
    x, y = xy
    return (x - y, x + y)


#############################
# 素数
#############################


def factorize(n):
    """
    nを素因数分解
    {素数: 数} のdictで返す
    計算量√N
    """
    d = defaultdict(int)
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            d[i] += 1
            n //= i
    if n > 1:
        d[n] = 1

    return d


#############################
# 累積和
#############################


def accumulate_2d(arr: List[List[int]]):
    """
    2次元累積和を計算する
    """

    n, m = len(arr), len(arr[0])

    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            acc[i][j] = (
                arr[i - 1][j - 1] + acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1]
            )

    return [row[1:] for row in acc[1:]]


#############################
# Main
#############################
N = int(input())

A = ["H", "D", "C", "S"]
B = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

S = [input() for _ in range(N)]


for i in range(N):
    L = [s for s in S if s == S[i]]
    if len(L) != 1:
        print("No")
        exit()

a = []

for i in range(N):
    if S[i][0] in A and S[i][1] in B:
        a.append(True)
    else:
        a.append(False)

print("Yes" if all(a) else "No")
