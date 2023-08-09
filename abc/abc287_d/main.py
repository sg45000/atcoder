S = input()
T = input()

s = len(S)
t = len(T)

post_memo = [False] * (t + 1)
post_memo[0] = True
back_memo = [False] * (t + 1)
back_memo[-1] = True

# S、Tの先頭から一文字ずつ同値判定をしていく。post_memoには同値判定の累積和を計上する
for i in range(t):
    matched = S[i] == '?' or T[i] == '?' or S[i] == T[i]
    post_memo[i + 1] = post_memo[i] & matched

# S、Tの末尾から一文字ずつ同値判定をしていく。back_memoには同値判定の累積和を計上する
for i in reversed(range(-t, 0)):
    matched = S[i] == '?' or T[i] == '?' or S[i] == T[i]
    back_memo[i - 1] = back_memo[i] & matched

for p, b in zip(post_memo, back_memo):
    if p & b:
        print("Yes")
    else:
        print("No")

