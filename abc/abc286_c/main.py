"""
Aの操作をまとめて行なった後にBをまとめて行うように考えても結果は同じなのでそのように考える。

文字数Nに対するAの操作はN回行うと同じ文章に戻るので、最大N回である
操作Aをi回行なった文章に対し、回文判定する文字同士が異なる場合にはBを支払う計算にする
このように回文かどうかのチェックを一文字ずつチェックしていくと
計算量は N * N // 2 = O(N^2)
"""

N, A, B = list(map(int, input().split(" ")))
S = input()

# 円環データ
S += S  # 文字を繋げるとAの操作に対して、見るインデックスを変えるだけで対応できる

ans = float('INF')
for i in range(N):
    price = i * A
    for j in range(N // 2):
        if S[i + j] != S[(N - 1) + i - j]:
            price += B
    ans = min(ans, price)

print(ans)