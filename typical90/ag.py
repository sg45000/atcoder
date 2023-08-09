"""
コーナーケースがある
不適切な状態とは、
イルミネーション全体に完全に含まれる 縦 2 * 横 2 の、4 つの LED を含む領域の中で、
点灯している LED が領域内に 2 つ以上あるものが存在する
という内容になっている。

つまり、縦 2 * 横 2の領域が存在しない場合は、不適切な状態は存在しない
"""

import math 

H, W = list(map(int, input().split(" ")))
if H == 1 or W == 1:
    print(max(H, W))
else:
    print(math.ceil(W / 2) * math.ceil(H / 2))

