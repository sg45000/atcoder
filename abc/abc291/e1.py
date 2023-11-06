from collections import deque
from typing import List


def topologicalSort(V: int, G: List[List[int]], indeg: List[int]):
    """
        DAGをトポロジカルソートしてくれるライブラリ
        V: 頂点数
        G: DAGのグラフ
        indeg: 各頂点の入次数
    """
    q = deque()

    # 1.入次数0の頂点を発見し、キューに追加
    for i in range(V):
        if indeg[i] == 0:
            q.append(i)
    
    sorted_list = []
    while q:
        v = q.popleft()
        sorted_list.append(v)  # キューの中の頂点は入次数が0の頂点なのでリストに追加

        for adj in G[v]:
            indeg[adj] -= 1  # 2. 入次数0の頂点から到達できる頂点の入次数を1減らす
            if indeg[adj] == 0:
                q.append(adj)  # 入次数0になったらキューに追加
    return sorted_list


N, M = list(map(int, input().split(" ")))

indeg = [0] * N
G = [[] for _ in range(N)]

for i in range(M):
    X, Y = list(map(int, input().split(" ")))
    X, Y = X - 1, Y - 1
    if Y in G[X]:
        continue
    G[X].append(Y)
    indeg[Y] += 1

# DAGであればトポロジカルソートして数列Aに並び変わるはず
a = topologicalSort(N, G, indeg)

# 数列Aを一意に特定できる条件は、トポロジカルソートした隣り合う頂点同士に繋がる辺があるかどうかで判定できる
for i in range(N - 1):
    if a[i + 1] not in G[a[i]]:
        print("No")
        exit()

ans = [""] * N
for i in range(N):
    ans[a[i]] = str(i + 1)

print("Yes")
print(*ans)
