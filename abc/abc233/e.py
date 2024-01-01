X = input()
length = len(X)
ACC = []

# 累積和を計算する
for x in X:
    x = int(x)
    if not ACC:
        ACC.append(x)
    else:
        ACC.append(ACC[-1] + x)

ans = []
carry = 0

# 逆順で処理する
for a in reversed(ACC):
    a += carry
    ans.append(str(a % 10))
    carry = a // 10

# 繰り上げが残っている場合
if carry > 0:
    ans.append(str(carry))

# リストを逆順にして文字列に結合する
print(''.join(reversed(ans)))