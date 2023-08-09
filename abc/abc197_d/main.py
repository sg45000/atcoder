"""
三角関数の問題

通常のtan関数は角度を入力として受け取り、その角度のタンジェントを返す
逆に、atan(アークタンジェント)はタンジェントを入力で受け取り、その角度を返す

正多角形の頂点は全て必ず円に接する。
(X0, Y0)と (Xn/2, Yn/2)の線分の中心が円の中心 = 多角形の中心になる。
円の中心を原点とした時、(X0, Y0)の角度θはatan2関数で求めることができる。
(X1, Y1)の角度θ' は角度θ + 2π / N となる。(正N角形の中心角は等しいので2π / N)
単位円で考えた時、角度θ'のsin, cosをとることで円の半径が1の時の(X1, Y1)を求められる。
この(X1, Y1)に元の正多角形が接している円の半径をかけることで、答えを求められる
"""
import math

N = int(input())
x0, y0 = list(map(int, input().split(" ")))
xn2, yn2 = list(map(int, input().split(" ")))


radius = math.sqrt((x0 - xn2) ** 2 + (y0 - yn2) ** 2) / 2
center_x = (x0 + xn2) / 2
center_y = (y0 + yn2) / 2

xy0angle = math.degrees(math.atan2(y0 - center_y, x0 - center_x))
xy1angle = xy0angle + (360 / N)

x1 = math.cos(math.radians(xy1angle))
y1 = math.sin(math.radians(xy1angle))

print(f"{center_x + x1 * radius} {center_y + y1 * radius}")