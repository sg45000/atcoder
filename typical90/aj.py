"""
マンハッタン距離を求める問題
点を全て45度回転する X = (x - y), Y = (x + y) となる

点(X1, Y1) から 点(X2, Y2) の マンハッタン距離は 
max(|X1 - X2|, |Y1 - Y2|)で求めることができる。

点(X1, Y1) から 最も遠い点までのマンハッタン距離は、
max(|X1 - X2|, |Y1 - Y2| ... |X1 - Xn|, |Y1 - Yn|)
で求めることができる

従って、クエリに答える前に Xn, Ynの最小値、最大値をそれぞれ求めておけば
各クエリに対し
max(|X1 - Xmax|, |Y1 - Ymax|, |X1 - Xmin|, |Y1 - Ymin|)
で答えを求めることができる

"""

N, Q = list(map(int, input().split(" ")))
xy = [list(map(int, input().split(" "))) for _ in range(N)]
qs = [int(input()) for _ in range(Q)]

X = []
Y = []

for x, y in xy:
    X.append(x - y)
    Y.append(x + y)

max_X = max(X)
max_Y = max(Y)

min_X = min(X)
min_Y = min(Y)

for q in qs:
    print(max(abs(X[q - 1] - max_X), abs(Y[q - 1] - max_Y), 
              abs(X[q - 1] - min_X), abs(Y[q - 1] - min_Y)))