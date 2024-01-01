from functools import reduce
from typing import Generic, List, Tuple, TypeVar
from itertools import chain

T = TypeVar("T")

#############################
# input
#############################

getInts = lambda: list(map(int, input().split()))

getChars = lambda: list(input())

#############################
# List
#############################


class FlexibleList(Generic[T], list):
    """
    Listを拡張したクラス
    initial_rangeを指定すると、その範囲のインデックスでアクセスできる
    """

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
    """
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
    """
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
    """
    指定した指定した矩形内の座標にtargetが含まれているかをチェックする
    """
    (sh, sw) = upper_left
    (gh, gw) = lower_right
    (th, tw) = target
    return sh <= th <= gh and sw <= tw <= gw


def linear_scan_n(
    grid: FlexibleList[FlexibleList[T]], n: int, d: (int, int), s: (int, int)
) -> List[Tuple[Coordinate, T]] | None:
    """
    gridの指定した数だけ直線に切り取る
    gridの範囲を超えた場合Noneを返す
    """
    ret = []
    for _ in range(n):
        try:
            ret.append(((s[0], s[1]), grid[s[0]][s[1]]))
            s = tuple([a + b for a, b in zip(d, s)])
        except IndexError:
            return None
    return ret


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


#############################
# Main
#############################
H, W = getInts()
grid = get_char_grid((1, 1), (H, W))

for i in range(1, H + 1):
    for j in range(1, W + 1):
        for d in [*vertical_dist(), *diagonal_dist()]:
            line = linear_scan_n(grid, 5, d, (i, j))
            if line is None:
                continue

            if all(["snuke"[k] == line[k][1] for k in range(5)]):
                for v, _ in line:
                    print(v[0], v[1])
                exit()

print("No")
