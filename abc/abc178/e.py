N = int(input())
XY = [list(map(int, input().split(' '))) for _ in range(N)]

# 座標を45°回転
def to_manhattan_dist(xy):
    x, y = xy
    return (x - y, x + y)


manhattan_XY = list(map(to_manhattan_dist, XY))

manhattan_X = sorted(map(lambda xy: xy[0], manhattan_XY))
manhattan_Y = sorted(map(lambda xy: xy[1], manhattan_XY))

# マンハッタン距離でX軸最大、Y軸最大の距離を取り大きいほうが答え
ans = max(abs(manhattan_X[0] - manhattan_X[-1]), abs(manhattan_Y[0] - manhattan_Y[-1]))
print(ans)