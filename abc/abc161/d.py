K = int(input())

dp = [""] * (K + 100)

# 初期値を入れておく(1 ~ 9)
for i in range(1, min(10, K + 1)):
    dp[i] = str(i)

# 初期値1から始める。
# その値の後ろにルンルンナンバーを足して、gが指すインデックスに更新
# ちなみにgで見ているインデックスはsで見ているインデックスより桁数が１つ大きい
s = 1  # 調べ始めるインデックス
g = 10  # 次に更新するインデックス
t = 10  # 調べ終わるインデックス
while g <= K:
    last = int(dp[s][-1])
    if last == 0:
        dp[g] = dp[s] + str(last)
        g += 1
        dp[g] = dp[s] + str(last + 1)
        g += 1
    elif 0 < last < 9:
        dp[g] = dp[s] + str(last - 1)
        g += 1
        dp[g] = dp[s] + str(last)
        g += 1
        dp[g] = dp[s] + str(last + 1)
        g += 1
    else:
        dp[g] = dp[s] + str(last - 1)
        g += 1
        dp[g] = dp[s] + str(last)
        g += 1
    
    s += 1
    if s == t:
        t = g

print(dp[K])
