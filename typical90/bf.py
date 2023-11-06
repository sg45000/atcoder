N, K = list(map(int, input().split(" ")))

D = [[0] * (10 ** 5) for _ in range(61)]

# 各整数が表示されていた場合にボタンAが1度だけ押された場合の表示を計算
for x in range(10 ** 5):
    y = 0
    for c in str(x):
        y += int(c)
    z = (x + y) % (10 ** 5)
    D[0][x] = z

# ダブリングで10^18回 相当まで計算
for i in range(60):
    for j in range(10 ** 5):
        D[i + 1][j] = D[i][D[i][j]]

# K回ボタンを押した時の表示をダブリングから求める
for bit in range(len(bin(K)) - 2):
    if K & 1 << bit:
        N = D[bit][N]

print(N)