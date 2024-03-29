"""
dp[l(左端の位置)][r(右端の位置)] = 対象の位置間の要素を取り除いた時の最小コスト とする
6 2 3 9 8 6 を例にとると
まず lとrの間の要素数0で考える。
6,2 2,3 3,9 ...といったサブセットの最小コストをdpに記録する

次にlとrの間の要素数2で考える。(この時要素数1としないのは、lrを含めた偶数個ずつしか取り除くことができないため)
6,2,3,9  2,3,9,8 ...といったサブセットの最小コストをそれぞれdpに記録する

あるサブセットの最小コストを考えるときは
1. lとrを同時に取り除いた場合
2. その他の場合
をそれぞれ考える必要がある
"""


N = int(input())
A = list(map(int, input().split(" ")))


dp = [[0] * 2 * N for _ in range(2 * N)]
for e in range(0, 2 * N - 2 + 1, 2):  # lr間に存在する要素の数
    for l in range(0, 2 * N - e - 1):
        r = l + e + 1
        # lとrを同時に取り除いた場合
        dp[l][r] = dp[l + 1][r - 1] + abs(A[l] - A[r])

        # その他の場合
        if e > 0:
            for k in range(l+1, r, 2):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])


print(dp[0][2*N - 1])