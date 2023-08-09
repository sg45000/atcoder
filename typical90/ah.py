"""
ナイーブに実装すると
区間の始端インデックスiをN回、区間の終端インデックスjをN回、探索するのでO(N^2)の計算量になってTLEする

そこでしゃくとり法の考えを元にとく
実際には、この問題は、区間の最大長を求めるので探索する区間長も広義単調増加としてよい
計算量O(N)で解ける
"""

from collections import defaultdict
from typing import Dict
N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

left = 0
right = 1

s = set()  # 指定区間 [left, right) に含まれる要素の種類数
node_count: Dict[int, int] = defaultdict(int)  # 指定区間 [left, right) に含まれる種類ごとの要素数
answer = 0  # 条件を満たす区間の最大長
while right <= N:
    # rightが示す要素を記録
    s.add(A[right - 1])
    node_count[A[right - 1]] += 1

    if len(s) > K:
        # 指定区間[left, right)が条件に合わない場合、区間を丸ごとシフト移動
        node_count[A[left]] -= 1
        if node_count[A[left]] == 0:
            s.remove(A[left])
        left += 1
        right += 1
    else:
        # 指定区間[left, right)が条件に合う場合は、右端を伸ばしてみて、次のループに持ち越す
        answer = right - left
        right += 1

print(answer)