"""
ランレングスで文字列を圧縮する
幸福じゃない人の数を計算する
幸福じゃない人は圧縮後の文字列の長さと一致する
一度の向き交換で2人幸せになる
"""


N, K = list(map(int, input().split(" ")))
S = input()

def encode(s):
    a = []
    a.append(s[0])
    for c in s[1:]:
        if a[-1] != c:
            a.append(c)
    return a

unhappy_len = len(encode(S))

for k in range(K):
    if 3 <= unhappy_len:
        unhappy_len -= 2
    elif unhappy_len == 2:
        unhappy_len = 1

print(N - unhappy_len)