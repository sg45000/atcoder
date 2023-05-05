import sys
 
sys.setrecursionlimit(1 << 30)
 
# m - f(m) = B
# m = f(m) + B  f(m)のmは昇順ソートした組み合わせ
"""
m - f(m) = B は、
m = f(m) + B に変換できる

f(m) は入力のmの桁ごとの数字を入れ替えても答えが同じ。
ex) f(8691) = 432, f(9618) = 432

昇順ソートされたm(= m')の組み合わせを一つずつ考える
m = f(m') + B と仮定すると
条件 m が N以下 かつ m' == sort(m) の時カウントを一つ増やす
"""

N, B = list(map(int, input().split(" ")))

ans = 0

def dfs(arranged_m, nex, fm):
    global ans
    if len(arranged_m) == 11: 
        return
    for i in range(nex, 10):
        new_arranged_m = arranged_m + str(i)
        new_fm = fm * i
        new_m = new_fm + B
        if new_m <= N and new_arranged_m == "".join(sorted(str(new_m))):
            ans += 1
        dfs(new_arranged_m, i, new_fm)

# 00 -> 000
# 01 -> 011
# 02
# 

dfs('', 0, 1)
print(ans)