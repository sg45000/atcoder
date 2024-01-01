"""
N < 2 * 10 ^ 5 なので全探索で解けるはず
ソート関数を使用するので計算量は O(N log N)
"""

N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]


def speech_effect(ab):
    a, b = ab
    # 演説を行うことで青木の投票がa票減り、高橋の投票がa + b票増えるので、
    # 実質的には、青木の投票がa票増え、高橋氏の投票が 2a + b票増えると言い換えられる
    return 2 * a + b

# 効果が大きい順にソートする
ab_ranking = sorted(AB, key=speech_effect, reverse=True)

a_sum = sum(a for a, _ in AB)

b_sum = 0
answer = 0
for ab in ab_ranking:  # 効果が大きい順に演説を行い、高橋氏の投票率が多くなればループ終了
    b_sum += speech_effect(ab)
    answer += 1
    if a_sum < b_sum:
        break
print(answer)
