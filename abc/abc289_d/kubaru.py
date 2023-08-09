"""
配るDPでとく
1段ずつその階段に到達できるかをメモする

計算量: O(XA) 10^6 
"""
N = int(input())
A = list(map(int, input().split(" ")))
M = int(input())
B = list(map(int, input().split(" ")))
X = int(input())

# dp初期化 階段iに到達できるか
dp = [False] * (X + 1)
dp[0] = True  # 0段目がスタートなのでTrue


b_memo = [True] * (X + 1)  # 餅で到達できないところのメモ。 到達できなければFalse
for b in B:
    b_memo[b] = False

for i in range(0, X):  # 一段ずつ到達できるか確認
    for a in A:
        # X段目までを考えればいいので、登る前のiからaだけ登った先がXを超えたら計算の必要なし
        # 餅があるところは無条件で到達不可
        if i + a > X or not b_memo[i + a]:
            continue
        dp[i + a] = dp[i + a] or dp[i]  # i + a段目には登れるルートが一つでもあればいいのでOR演算

print("Yes") if dp[X] else print("No")
    