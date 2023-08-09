"""
各マスを全探索

一つ上のマスの上下方向の明かりが点る数
一つ左のマスの左右方向の明かりが点る数
は今のマスと地続きの場合に参考にできる
"""

H, W = list(map(int, input().split(" ")))
S = [input() for _ in range(H)]

dp = [[(0, 0)] * (W + 1) for _ in range(H + 1)]
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        
        if dp[h][w + 1][0] == 0:  # 一つ上のマスが＃だった場合
            for next_h in range(h, H):
                if S[next_h][w] == "#":
                    break
                else:
                    i, j = dp[h + 1][w + 1]
                    dp[h + 1][w + 1] = (i + 1, j)
        else:
            dp[h + 1][w + 1] = (dp[h][w + 1][0], dp[h + 1][w + 1][1])
        
        if dp[h + 1][w][1] == 0:  # 一つ左のマスが＃だった場合
            for next_w in range(w, W):
                if S[h][next_w] == "#":
                    break
                else:
                    i, j = dp[h + 1][w + 1]
                    dp[h + 1][w + 1] = (i, j + 1)
        else:
            dp[h + 1][w + 1] = (dp[h + 1][w + 1][0], dp[h + 1][w][1])

answer = 0
for a in dp:
    for i, j in a:
        answer = max(answer, i + j)

print(answer - 1)