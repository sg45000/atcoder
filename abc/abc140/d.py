"""
ランレングスで文字列を圧縮する
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