"""

"""

import math

T = int(input())
L, X, Y = list(map(int, input().split(" ")))
Q = int(input())

radius = L / 2  # 半径

for _ in range(Q):
    E = int(input())
    sy = -radius * math.sin(math.radians(360 * E / T))  # 添乗者のY軸の位置
    sz = radius - radius * math.cos(math.radians(360 * E / T))  # 添乗者のZ軸の位置
    A = math.sqrt(X ** 2 + (sy - Y) ** 2)  # 水平平面上の添乗者と像の距離
    B = sz  # 垂直方向上の添乗者と象の距離
    print(math.degrees(math.atan2(B, A)))

# print(math.sin(math.radians(45)))
# print(math.degrees(math.atan2(1,1)))