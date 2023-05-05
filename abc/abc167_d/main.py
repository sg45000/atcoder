
def main(N, K, towns):
    i = 0
    k = 0
    visited_count = [0] * N
    visited = []
    while True:
        k = k + 1  # 移動回数をインクリメント

        if k == K:  # ループの前に移動回数に達したら答えを返却
            return towns[i]
        visited_count[i] += 1  # 訪れた回数を記録しておく
        if visited_count[i] == 2:  # ２度目はループに入ったということ
            break
        visited.append(i)
        i = towns[i] - 1

    K = K - len(visited)  # ループする前の移動回数を全移動回数からひいておく
    loop = visited[visited.index(i):]  # ループ順番のリストを取り出す
    mod = K % len(loop)  # ループの最後の周回の移動回数を取り出す
    return loop[mod] + 1


N, K = map(int, input().split())
towns = list(map(int, input().split()))

print(main(N, K, towns))
# print(main(4, 3, [3, 2, 4, 1]))