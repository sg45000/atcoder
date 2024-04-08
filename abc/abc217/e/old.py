"""
優先度付キューは取り出しと挿入をO(logN)で行うことができる
"""

from collections import deque
import heapq

Q = int(input())


D = deque()

SD = []
heapq.heapify(SD)

for _ in range(Q):
    q = list(map(int, input().split(" ")))
    if q[0] == 1:
        # 計算量O(1)
        D.append(q[1])
    elif q[0] == 2:
        if len(SD) > 0:
            # 計算量O(logQ)
            print(heapq.heappop(SD))
        else:
            # 計算量O(1)
            print(D.popleft())
    else:
        # 最悪計算量 (QlogQ)
        while D:
            heapq.heappush(SD, D.popleft())
