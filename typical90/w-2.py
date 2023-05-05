"""
bitDPで解く
dp[行][その行のkingの位置を表すbit]
"""

H, W = list(map(int, input().split(" ")))
C = [list(input()) for _ in range(H)]
modulus = 10 ** 9 + 7

def is_valid(b, h):
    for i in range(W):  # kingを置ける場所にビットが立っているか
        if b >> i & 1 and C[h][i] == '#':
            return False
    for i in range(W - 1):  # kingが同じ行で隣り合ってないか
        if b >> i & b >> (i + 1):
            return False
    return True

dp = [[0] * (2 ** (W)) for _ in range(H + 1)]

for h in range(H):  # 一行ずつdpで解く
    for b1 in range(2 ** W):
        if not is_valid(b1, h):
            continue
        if h == 0:  # hが1行目の場合は、全て通り数1
            dp[h + 1][b1] = 1
            continue
        
        for b0 in range(2 ** W): # 一つ前の行のbit列
            # bit列同士でNANDを取りkingが隣り合ってないか判定する
            # 片方のbit列を1つ左右にスライドさせたものとも比較する
            if all(map(lambda x: x == bin(-1), [bin(~(b0 & b1)), bin(~(b0 >> 1 & b1)), bin(~(b0 << 1 & b1))])):
                dp[h + 1][b1] += (dp[h][b0] % modulus)
                dp[h + 1][b1] %= modulus

answer = 0
for i in range(2 ** W):
    answer += (dp[-1][i] % modulus)
    answer %= modulus
print(answer)

