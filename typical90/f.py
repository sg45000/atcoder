N, K = list(map(int, input().split(" ")))
S = input()

start = 0
end = N - K + 1
answer = ''

# 答えを一文字ずつ探索
for _ in range(K):
    min_c = 'zz'
    min_i = 0
    # 全探索して辞書順最小の文字を答えに追加していく
    for i, c in enumerate(S[start:end]):
        if c < min_c:
            min_i = i
            min_c = c
    answer += min_c
    start += min_i + 1
    end += 1

print("".join(answer))
