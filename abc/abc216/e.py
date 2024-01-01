"""
等差数列の和 の公式を使う

貪欲法で解く

"""

N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A.sort(reverse=True)

def f(x, k):
    return ((x * (1 + x)) // 2) - (((x - k) * (1 + x - k)) // 2)
    
# 数列Aの合計がK以下の場合は全て足し合わせればOK
if sum(A) <= K:
    ans = 0
    for a in A:
        ans += f(a, a)
    print(ans)
    exit()


ans = 0

for i in range(N - 1):
    diff = A[i] - A[i + 1]
    cnt = diff * (i + 1)

    if cnt <= K:
        K -= cnt
        ans += f(A[i], diff) * (i + 1)
    else:
        j = K // (i + 1)  # 引く回数
        ans += f(A[i], j) * (i + 1)
        ans += (A[i] - j) * (K % (i + 1))
        K = 0
print(ans)