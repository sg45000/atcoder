"""
'a'と'b'の並び順の通り数は、2次元座標にして考えるといい
(0, 0)から始まりx軸の正の方向あるいはy軸の正の方向に1進むことを繰り返すことで(x, y)がそのままaがx個、bがy個あった時の通り数になる。
これは動的計画法で求められる

辞書順が関係する問題は、前の文字から決めていくのが定石らしい。
aを先頭にした場合の通り数を(前述のdpより)計算して、その数がK以上であればK番目の文字列はaが先頭であることがわかる

それを繰り返していくことで最終的な文字列が浮かび上がる
"""

A, B, K = list(map(int, input().split(" ")))

dp = [[0] * (B + 1) for _ in range(A + 1)]
dp[0][0] = 1

for a in range(A):
    dp[a + 1][0] = 1
for b in range(B):
    dp[0][b + 1] = 1

for a in range(A):
    for b in range(B):
        dp[a + 1][b + 1] = dp[a + 1][b] + dp[a][b + 1]

ans = ""
for _ in range(A + B):
    if 0 < A:
        if K <= dp[A - 1][B]:
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= dp[A - 1][B]
            B -= 1
    else:
        ans += 'b'
        B -= 1

print(ans)