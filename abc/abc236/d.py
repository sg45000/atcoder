"""
全探索で求まる
2Nの長さのbitで組み合わせに使った人を表している

"""

N = int(input())
A = [[0] * (2 * N) for _ in range(2 * N - 1)]

for i in range(2 * N - 1):
    a = list(map(int, input().split(" ")))
    for j, c in enumerate(a):
        A[i][j + i + 1] = c

ans = 0
# この関数は一つの組みを探索
def calc(S, score):
    global ans
    if S == (1 << (2 * N)) - 1:
        ans = max(ans, score)
        return
    first = -1
    for i in range(2 * N):
        if S >> i & 1:
            continue
        if first == -1:
            first = i  # 最初の一人目を選ぶ
            S |= 1 << first
        else:
            calc(S | 1 << i, score ^ A[first][i])  # 二人目を選び計算次の組みを探索

calc(0, 0)
print(ans)