"""
クエリ2で袋に入ってるボールを全て更新してると時間が間に合わない
なので、クエリ2で足される数値を記録しておき、クエリ1で新しく追加するボールはその記録した数値を引いてあげる
あとは優先度つきキュー
"""
import heapq
Q = int(input())

bag = []
heapq.heapify(bag)
plus = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(bag, q[1] - plus)
    elif q[0] == 2:
        plus += q[1]
    else:
        print(heapq.heappop(bag) + plus)
