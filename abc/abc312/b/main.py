
from typing import List, Tuple

#############################
# input
#############################

getInts = lambda: list(map(int, input().split()))

getChars = lambda: list(input())

#############################
# List
#############################


class FlexibleList(list):
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


    def at(self, index):
        if index < self.begin or index > self.end:
            raise IndexError("Index out of range")
        return self[index - self.begin]



#############################
# Grid
#############################


GridCoordinate = Tuple[int, int]


def get_char_grid(upper_left: GridCoordinate, lower_right: GridCoordinate) -> FlexibleList[FlexibleList[int]]:
    """_summary_
    文字で構成されたグリッドを読み込み2次元配列で返す
    """
    (ulh, ulw) = upper_left
    (lrh, lrw) = lower_right
    return FlexibleList([FlexibleList(getChars(), (ulw, lrw)) for _ in range(lrh + 1 - ulh)], (ulh, lrh))


def create_grid_range(upper_left: GridCoordinate, lower_right: GridCoordinate) -> List[GridCoordinate]:
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


def in_range(upper_left: GridCoordinate, lower_right: GridCoordinate, target: GridCoordinate) -> bool:
    """_summary_
    指定した指定した矩形内の座標にtargetが含まれているかをチェックする
    """
    (sh, sw) = upper_left
    (gh, gw) = lower_right
    (th, tw) = target
    return sh <= th <= gh and sw <= tw <= gw


N, M = getInts()

grid = get_char_grid((1, 1), (N, M))

tak_code = """
###.?????
###.?????
###.?????
....?????
?????????
?????....
?????.###
?????.###
?????.###
"""

rects: List[Tuple[Tuple[int, int], List[str]]] = []

for i in range(1, N + 1):
    for j in range(1, M + 1):
        coods = create_grid_range((i, j), (i + 8, j + 8))
        rect = []
        for v in coods:
            if in_range((1, 1), (N, M), v):
                rect.append(grid.at(v[0]).at(v[1]))
        if len(rect) == 81:
            rects.append(((i, j), rect))

for v, rect in rects:
    if all([a == "?" or a == b for a, b in zip(tak_code.replace("\n", ""), rect)]):
        print(v[0], v[1])
