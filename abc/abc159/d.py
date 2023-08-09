from collections import defaultdict
from functools import reduce

N = int(input())
A = list(map(int, input().split(" ")))

D = defaultdict(int)

def combination_of_two(v):
    return (v * (v - 1) // 2)

for a in A:
    D[a] += 1

# 全てのボールがある時の場合の和を計算
s = reduce(lambda acc, v: acc + combination_of_two(v), [0] + list(D.values()))  # reduceは初期値を指定できないので渡すリストの最初に単位元を追加

for a in A:
    print(s - combination_of_two(D[a]) + combination_of_two(D[a] - 1))  # 各ボールがない場合の場合の和を計算