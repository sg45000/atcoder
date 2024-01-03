from functools import reduce
from typing import Generic, List, Set, Tuple, TypeVar
from itertools import chain, count

T = TypeVar("T")

#############################
# input
#############################

getInts = lambda: list(map(int, input().split()))

getChars = lambda: list(input())

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
    upper_left: Coordinate, lower_right: Coordinate
) -> FlexibleList[FlexibleList[int]]:
    """_summary_
    文字で構成されたグリッドを読み込み2次元配列で返す
    """
    (ulh, ulw) = upper_left
    (lrh, lrw) = lower_right
    return FlexibleList(
        [FlexibleList(getChars(), (ulw, lrw)) for _ in range(lrh + 1 - ulh)], (ulh, lrh)
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


#############################
# GridSet
#############################

GridSet = Set[Coordinate]


def to_gs(coords: List[Coordinate]) -> GridSet:
    """
    座標のリストをGridSetに変換
    """
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
# Main
#############################


N = int(input())
grid = get_char_grid((0, 0), (N - 1, N - 1))

ans = 0
for i in range(N):
    for j in range(N):
        vs = to_gs(range_to_coords((i, j), (i + N - 1, j + N - 1)))
        for v in vs:
            for d in [*vertical_dist(), *diagonal_dist()]:
                line = linear_scan_n_gs(vs, N, d, v)
                if line is None:
                    continue
                default_indexes = [ixmap(v, N, N) for v in line]
                ans = max(ans, int("".join([grid[i][j] for i, j in default_indexes])))

print(ans)
