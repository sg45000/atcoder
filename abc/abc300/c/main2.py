H, W = list(map(int, input().split(" ")))

S = [input() for _ in range(H)]

point = 0
# 4マスの塊ずつ見ていって、黒マスが1つか3つの塊の真ん中が頂点
for i in range(H - 1):
    for j in range(W - 1):
        black = 0
        for x, y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if S[i + y][j + x] == "#":
                black += 1
        if black == 1 or black == 3:
            point += 1

print(point)
