"""
!10 = 3628800 == O(10^6)
コストの計算にO(10^1)

仲が悪い判定をするのに最大M(およそ45 == O(10 ^ 1))

なのでO(10^8 ~ 9)程度。5秒あるので全探索でいけそう
"""

import itertools
from collections import defaultdict

N = int(input())
A = [list(map(int, input().split(" "))) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split(" "))) for _ in range(M)]

P = itertools.permutations(range(N))

bad_relations = defaultdict(list) # 仲が悪いリストを辞書にしてO(1)で引けるようにしておく
for x, y in XY:
    bad_relations[x - 1].append(y - 1)
    bad_relations[y - 1].append(x - 1)

min_cost = float("INF")
for p in P:
    cost = 0
    bad = []
    can_finish = True

    for order, player in enumerate(p):
        # 前走者の仲が悪いリストに入ってるかどうかだけ判定
        # いずれかが仲が悪ければこのpermutationは完走できない
        if any(player == b for b in bad):
            can_finish = False
            break
        bad = bad_relations[player]  # 次の走者の判定のために自分の仲が悪いリストを入れておく

        cost += A[player][order]

    if can_finish:
        min_cost = min(cost, min_cost)

if min_cost == float("INF"):
    print(-1)
else:
    print(min_cost)
