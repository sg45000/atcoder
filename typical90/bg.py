N, M, Q = list(map(int, input().split(" ")))
XY = [list(map(int, input().split(" "))) for _ in range(M)]
AB = [list(map(int, input().split(" "))) for _ in range(Q)]

adj = [[] for _ in range(N)]
for x, y in XY:
    adj[y - 1].append(x - 1)

K = 1000 # 一気に処理するクエリ数 (MLEしなければいくつでも)
for i in range(Q // K + 1):
    ab = AB[i * K: i * K + K]
    dp = [0] * N
    # 初期化 各クエリのスタート頂点のビットを立てる
    for k, (a, b) in enumerate(ab):
        dp[a - 1] |= 1 << k
    # 到達可能頂点の計算
    for v in range(N):
        for u in adj[v]:
            dp[v] |= dp[u]
    # クエリ毎の結果を求める
    for k, (a, b) in enumerate(ab):
        print("Yes" if dp[b - 1] & (1 << k) else "No")
