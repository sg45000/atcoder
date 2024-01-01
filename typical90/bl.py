"""
地殻変動に対して、区画1つ1つの高さを更新していくと間に合わない

地殻変動があった範囲の隣の区画との差異だけを考えていけば、O(Q)で求められる
例えばLが1のときは、R側だけの差が発生するので、そのdiffを更新する
"""

N, Q = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))


# diffには最初と最後に0を入れておいて、計算しやすいようにしておく
diff = [0]

ans = 0
for i in range(N - 1):
    diff.append(A[i + 1] - A[i])
    ans += abs(diff[i + 1])

diff.append(0)


for _ in range(Q):
    L, R, V = list(map(int, input().split(" ")))

    a = abs(diff[L - 1]) + abs(diff[R])

    if L > 1:
        diff[L - 1] += V
    if R < N:
        diff[R] -= V

    b = abs(diff[L - 1]) + abs(diff[R])

    ans += b - a
    print(ans)